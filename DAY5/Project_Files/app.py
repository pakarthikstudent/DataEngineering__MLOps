from flask import Flask, request, jsonify
import time
import joblib
import numpy as np
import logging
import psutil
import threading
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__) 

# Load trained model
model = joblib.load("model.pkl")

# Logging configuration
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Prometheus metrics
REQUEST_COUNT = Counter("app_requests_total", "Total number of requests")
INFERENCE_TIME = Histogram("app_inference_time_seconds", "Time taken for model inference")
CPU_USAGE = Gauge("app_cpu_usage_percent", "Current CPU usage percentage")
MEMORY_USAGE = Gauge("app_memory_usage_percent", "Current Memory usage percentage")

def collect_system_metrics():
    """Background thread to update CPU and memory usage"""
    while True:
        CPU_USAGE.set(psutil.cpu_percent(interval=1))
        MEMORY_USAGE.set(psutil.virtual_memory().percent)
        time.sleep(5)  # Update every 5 seconds

# Start metrics collection in a background thread
threading.Thread(target=collect_system_metrics, daemon=True).start()

@app.route("/predict", methods=["POST"])
def predict():
    REQUEST_COUNT.inc()  # Increment request count
    start_time = time.time()

    try:
        data = request.json["features"]  # Expecting a JSON payload with "features"
        features = np.array(data).reshape(1, -1)

        prediction = model.predict(features)[0]  # Get the class prediction
        response_time = time.time() - start_time
        INFERENCE_TIME.observe(response_time)  # Record inference time

        result = {"prediction": int(prediction), "time_taken": round(response_time, 4)}
        logging.info(f"Input: {data}, Prediction: {result}, Response Time: {response_time:.4f}s")

        return jsonify(result)

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 400

# Prometheus metrics endpoint
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

# Health check
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
