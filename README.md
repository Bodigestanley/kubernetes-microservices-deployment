# 🚀 Kubernetes Microservices Deployment Project

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Container-blue.svg)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue.svg)](https://kubernetes.io/)
[![Minikube](https://img.shields.io/badge/Minikube-LocalCluster-yellowgreen.svg)](https://minikube.sigs.k8s.io/)

---

## 🔹 Project Overview

This project demonstrates a **complete microservices architecture** using:

- **Flask** (Python web framework)  
- **Docker** (Containerization)  
- **Kubernetes** (Container orchestration)  
- **Minikube** (Local Kubernetes cluster)  

The architecture consists of **4 microservices**:

1. **Auth Service** – Handles authentication  
2. **Product Service** – Manages products  
3. **Order Service** – Handles orders  
4. **Frontend Service** – Provides a simple UI  

All services are containerized and deployed on Kubernetes using **Deployments, Services, and Ingress**.

---

## 🔹 Architecture Diagram

![Architecture Diagram](./screenshots/architecture.png)  
*(Frontend Service → Auth / Product / Order Services)*

---

## 🔹 Features

- Multi-service Flask applications  
- Dockerized microservices  
- Kubernetes deployments with replicas  
- NodePort Services for each microservice  
- Ingress setup for routing multiple services via a single URL  
- Minikube used for local testing  
- Fully automated deployment with `kubectl apply -f .`  

---

## 🔹 Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)  
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)  
- [kubectl](https://kubernetes.io/docs/tasks/tools/)  

---

## 🔹 How to Run Locally

### 1. Build Docker images

```bash
docker build -t auth-service ./auth-service
docker build -t product-service ./product-service
docker build -t order-service ./order-service
docker build -t frontend-service ./frontend
