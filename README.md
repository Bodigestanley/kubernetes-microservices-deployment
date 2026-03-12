# 🚀 Kubernetes Microservices Deployment Project

![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red)
![Python](https://img.shields.io/badge/Python-Flask-green)
![DevOps](https://img.shields.io/badge/DevOps-Automation-orange)

This project demonstrates a **complete Kubernetes microservices architecture** with DevOps practices. The microservices include **Auth, Product, Order, and Frontend**, containerized with Docker, deployed on **Kubernetes (Minikube)**, and automated using **CI/CD pipelines**.

---

## 📌 Architecture Diagram

![Architecture Diagram](docs/kubernetes_microservices_architecture.png)

**Flow:**

Developer
│
▼
GitHub Repository
│
▼
Jenkins CI/CD Pipeline
│
▼
Docker Build
│
▼
Docker Containers
│
▼
Kubernetes Cluster (Minikube)
│
▼
Auth Service ↔ Product Service ↔ Order Service
↕
Frontend Service


---

## 🛠 Technologies Used

* Python (Flask)
* Docker
* Kubernetes (Minikube)
* Jenkins
* Git & GitHub

---

## 📂 Project Structure

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
├── k8s/
│ ├── auth-deployment.yaml
│ ├── product-deployment.yaml
│ ├── order-deployment.yaml
│ ├── frontend-deployment.yaml
│ └── services.yaml
├── docs/
│ ├── jenkins-pipeline.png
│ ├── docker-containers.png
│ ├── kubernetes-pods.png
│ └── kubernetes_microservices_architecture.png
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Bodigestanley/kubernetes-microservices-deployment.git
cd kubernetes-microservices-project
2️⃣ Build Docker Images
docker build -t auth-service ./auth-service
docker build -t product-service ./product-service
docker build -t order-service ./order-service
docker build -t frontend-service ./frontend-service
3️⃣ Start Minikube
minikube start
4️⃣ Deploy Microservices to Kubernetes
kubectl apply -f k8s/
5️⃣ Verify Deployments
kubectl get pods
kubectl get services
6️⃣ Access Frontend Service
minikube service frontend-service
🔄 CI/CD Pipeline (Jenkins)

The Jenkins pipeline automates:

Clone repository from GitHub

Build Docker images

Push images (optional: Docker Hub)

Deploy containers to Kubernetes

Pipeline configuration is defined in Jenkinsfile.

📸 Project Screenshots














Screenshots show each microservice running in Minikube.

🚀 Future Improvements

Push Docker images to Docker Hub

Deploy to AWS EC2 / EKS

Add Ingress Gateway for routing

Integrate monitoring with Prometheus & Grafana

Implement real authentication & database backend

👨‍💻 Author

Stanley Bodige
DevOps | Cloud | Cybersecurity Enthusiast

GitHub: https://github.com/Bodigestanley
