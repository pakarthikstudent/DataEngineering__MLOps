
# Real-Time ML Model Monitoring and Logging with Prometheus & Grafana

This project demonstrates how to build a **real-time monitoring system** for a machine learning model deployed using **Flask**, with observability powered by **Prometheus** and **Grafana**. It provides production-grade insight into inference metrics, system resource usage, and operational health of your ML service.

## 🚀 Features

- Real-time tracking of ML inference requests
- Latency monitoring via Prometheus histograms
- CPU and memory usage tracking with `psutil`
- Visual dashboards with Grafana
- Lightweight Flask server with `/predict`, `/metrics`, and `/health` endpoints
- Model training on Iris dataset using RandomForestClassifier

## 📦 Tech Stack

- Flask  
- Scikit-learn, joblib  
- Prometheus  
- Grafana  
- psutil  
- Python Logging  

## 📁 Project Structure

```
├── app.py                 # Flask server with Prometheus metrics
├── model.pkl              # Pre-trained ML model
├── train_model.py         # Script to train and save the model
├── prometheus.yml         # Prometheus configuration file
└── README.md              # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.x
- Homebrew (for macOS users)
- Prometheus & Grafana

### Install Python Packages

```bash
pip install flask joblib psutil prometheus_client scikit-learn
```

### Train Model

```bash
python train_model.py
```

### Start Flask App

```bash
python app.py
```

### Start Prometheus

```bash
prometheus --config.file=prometheus.yml
```

### Start Grafana

```bash
brew services start grafana
```

Then visit:

- Prometheus: [http://localhost:9090](http://localhost:9090)  
- Grafana: [http://localhost:3000](http://localhost:3000) (login: `admin` / `admin`)

##  Metrics Visualized in Grafana

- Total Inference Requests  
- Inference Latency (seconds)  
- CPU Usage (%)  
- Memory Usage (%)  

##  Future Improvements

- Model accuracy & drift tracking  
- Integration with Kubernetes & autoscaling  
- Advanced logging & tracing (e.g., ELK, Jaeger)


