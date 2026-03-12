# 🚀 Kubernetes Microservices Deployment Project

![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue)
![Python](https://img.shields.io/badge/Python-Flask-green)
![DevOps](https://img.shields.io/badge/DevOps-Automation-orange)

This project demonstrates a **full DevOps workflow** with a **microservices architecture**, using Python Flask apps, Docker, and Kubernetes. It includes **Auth, Product, Order, and Frontend services**, deployed on **Minikube** with a CI/CD pipeline.

---

# 📌 Architecture Diagram

                    ┌─────────────┐
                    │  Developer  │
                    └─────┬───────┘
                          │
                          ▼
               ┌─────────────────────┐
               │ GitHub Repository   │
               └─────────┬──────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Jenkins CI/CD   │
                │ Pipeline        │
                └─────────┬───────┘
                          │
                          ▼
                    ┌─────────┐
                    │ Docker  │
                    │ Build   │
                    └────┬────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Kubernetes    │
                 │ Cluster       │
                 └───────────────┘
      ┌─────────────┬─────────────┬─────────────┬─────────────┐
      ▼             ▼             ▼             ▼

┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Auth Service│ │ Product Svc │ │ Order Svc │ │ Frontend Svc│
└─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘


![Kubernetes Architecture](docs/k8s-architecture.png)

---

# 🛠 Technologies Used

* **Python 3.14** (Flask)
* **Docker**
* **Kubernetes (Minikube)**
* **Jenkins CI/CD**
* **Git & GitHub**
* **HTML/CSS for microservice pages**

---

# 📂 Project Structure


kubernetes-microservices-project/
│
├── auth-service/
│ └── app.py
├── product-service/
│ └── app.py
├── order-service/
│ └── app.py
├── frontend-service/
│ └── app.py
├── kubernetes/
│ ├── auth-deployment.yaml
│ ├── product-deployment.yaml
│ ├── order-deployment.yaml
│ ├── frontend-deployment.yaml
│ └── services.yaml
├── docs/
│ ├── auth-service.png
│ ├── product-service.png
│ ├── order-service.png
│ ├── frontend-service.png
│ └── k8s-architecture.png
└── README.md


---

# ⚙️ Setup Instructions

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bodigestanley/kubernetes-microservices-deployment.git
cd kubernetes-microservices-project
2️⃣ Build Docker Images
docker build -t auth-service ./auth-service
docker build -t product-service ./product-service
docker build -t order-service ./order-service
docker build -t frontend-service ./frontend-service
3️⃣ Deploy to Kubernetes

Start Minikube:

minikube start

Deploy microservices:

kubectl apply -f kubernetes/

Check running pods and services:

kubectl get pods
kubectl get services

Open services in browser:

minikube service auth-service
minikube service product-service
minikube service order-service
minikube service frontend-service
📸 Microservice Screenshots

Auth Service:


Product Service:


Order Service:


Frontend Service:


🔄 Jenkins CI/CD Pipeline

The Jenkins pipeline includes:

Clone repo from GitHub

Build Docker images for all microservices

Run containers

Deploy to Kubernetes (Minikube)

Pipeline configuration is defined in Jenkinsfile.

🚀 Future Improvements

Push Docker images to Docker Hub

Deploy Kubernetes cluster on AWS EKS

Add Prometheus & Grafana monitoring

Integrate API Gateway for microservices

Add database integration and authentication

👨‍💻 Author

Stanley Bodige
DevOps | Cloud | Cybersecurity Enthusiast

GitHub: https://github.com/Bodigestanley


✅ **Next Steps:**  

1. Make sure all screenshots (`auth-service.png`, `product-service.png`, `order-service.png`, `frontend-service.png`) and `k8s-architecture.png` are in `docs/`.  
2. Save this as **README.md** in your repo root.  
3. Commit & push:

```bash
git add docs/ README.md
git commit -m "Add polished README with architecture and screenshots"
git push origin main
