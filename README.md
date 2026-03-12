# 🚀 Kubernetes Microservices Deployment Project

![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red)
![Python](https://img.shields.io/badge/Python-Flask-green)
![DevOps](https://img.shields.io/badge/DevOps-Automation-orange)

This project demonstrates a **full Kubernetes microservices architecture** with **DevOps CI/CD practices**. It includes **4 Flask microservices**:

- Auth Service  
- Product Service  
- Order Service  
- Frontend Service  

Each service is containerized using **Docker** and deployed to **Kubernetes (Minikube)**.

---

# 📌 Architecture Diagram

![Architecture Diagram](docs/k8s-architecture.png)

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
Docker Build & Push
│
▼
Docker Containers
│
▼
Kubernetes Cluster (Minikube)
│
▼
Auth / Product / Order / Frontend Services


---

# 🛠 Technologies Used

* **Python (Flask)**
* **Docker**
* **Kubernetes (Minikube)**
* **Jenkins CI/CD**
* **Git & GitHub**

---

# 📂 Project Structure


kubernetes-microservices-project
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
│ ├── deployment.yaml
│ └── service.yaml
├── docs/
│ ├── auth-service.png
│ ├── product-service.png
│ ├── order-service.png
│ ├── frontend-service.png
│ └── k8s-architecture.png
└── README.md


---

# ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bodigestanley/kubernetes-microservices-deployment.git
cd kubernetes-microservices-project
2️⃣ Build Docker Images
docker build -t auth-service ./auth-service
docker build -t product-service ./product-service
docker build -t order-service ./order-service
docker build -t frontend-service ./frontend-service
3️⃣ Run Docker Containers (Optional for Testing Locally)
docker run -p 5001:80 auth-service
docker run -p 5002:80 product-service
docker run -p 5003:80 order-service
docker run -p 5000:80 frontend-service
☸ Kubernetes Deployment

Start Minikube:

minikube start

Deploy all microservices:

kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

Check running pods:

kubectl get pods

Check services:

kubectl get services

Open any service:

minikube service frontend-service
🔄 Jenkins CI/CD Pipeline

The Jenkins pipeline includes stages:

Clone repo from GitHub

Build Docker images for all microservices

Push images (optional)

Deploy containers to Kubernetes cluster

Pipeline configuration is defined in Jenkinsfile.

📸 Project Screenshots

Auth Service:


Product Service:


Order Service:


Frontend Service:


🚀 Future Improvements

Push Docker images to Docker Hub automatically

Deploy to cloud Kubernetes (AWS EKS / GCP GKE)

Add Prometheus + Grafana monitoring

Add CI/CD notifications to Slack / Teams

👨‍💻 Author

Stanley Bodige
DevOps | Cloud | Microservices Enthusiast

GitHub: https://github.com/Bodigestanley


---

✅ **Instructions for your repo**:

1. Place your **screenshots** (`auth-service.png`, `product-service.png`, `order-service.png`, `frontend-service.png`) and `k8s-architecture.png` in the `docs/` folder.  
2. Save this content as **README.md** in the root of your repo.  
3. Add, commit, and push:

```bash
git add docs/ README.md
git commit -m "Add polished README with architecture and screenshots"
git push origin main
