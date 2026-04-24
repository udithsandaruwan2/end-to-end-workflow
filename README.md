# 🚀 End-to-End Django CI/CD Deployment (Docker + AWS + Traefik)

A production-ready backend system built with **Django**, containerized using **Docker**, deployed on **AWS EC2**, and fully automated using **GitHub Actions CI/CD** with **Traefik reverse proxy**.

---

# 📌 Overview

This project demonstrates a complete modern DevOps workflow:

* Django REST backend
* PostgreSQL database
* Dockerized microservice architecture
* Traefik reverse proxy for routing
* AWS EC2 deployment
* CI/CD pipeline with GitHub Actions
* Automatic deployment on push to `main`

---

# 🧠 System Architecture

## 🔷 High-Level Flow

```
User Browser
     ↓
Public IP / Domain (AWS EC2)
     ↓
Traefik Reverse Proxy
     ↓
Django Application (Gunicorn)
     ↓
PostgreSQL Database
```

---

## 🔷 CI/CD Flow

```
Developer Push → GitHub Repo
        ↓
GitHub Actions (CI/CD Pipeline)
        ↓
Run Tests + Validate Django
        ↓
SSH into AWS EC2
        ↓
Git Pull Latest Code
        ↓
Docker Compose Rebuild
        ↓
Application Updated
```

---

# 🏗️ Tech Stack

* 🐍 Django (Backend API)
* 🐳 Docker & Docker Compose
* ⚡ Traefik (Reverse Proxy)
* 🐘 PostgreSQL (Database)
* ☁️ AWS EC2 (Deployment Server)
* 🔁 GitHub Actions (CI/CD)
* 🔧 uv (Python dependency manager)

---

# 📁 Project Structure

```
end-to-end-workflow/
│
├── backend/
├── api/
├── users/
├── templates/
├── staticfiles/
│
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# 🚀 Deployment Architecture

## 🖥️ AWS EC2 Setup

* Ubuntu server (t3.micro)
* Public IP exposed
* Docker installed
* Git installed
* Security group configured

### Open Ports:

* 80 → Traefik HTTP
* 8080 → Traefik Dashboard
* 5432 → PostgreSQL (internal only)

---

## 🐳 Docker Services

### 1️⃣ Django App

* Runs via Gunicorn
* Exposed internally on port `8000`
* Handles all API requests

---

### 2️⃣ PostgreSQL Database

* Official PostgreSQL image
* Persistent volume storage
* Internal Docker network only

---

### 3️⃣ Traefik Reverse Proxy

* Routes external traffic
* Auto-discovers services via Docker
* Dashboard enabled on port `8080`

---

# 🌐 Access URLs

After deployment:

### 🔥 Main Application

```
http://<EC2_PUBLIC_IP>/
```

### 📊 Traefik Dashboard

```
http://<EC2_PUBLIC_IP>:8080/dashboard/
```

---

# 🔐 CI/CD Pipeline (GitHub Actions)

## Trigger

* Runs on every push to `main`

## Pipeline Steps

1. Checkout code
2. Setup Python 3.12
3. Install uv
4. Install dependencies
5. Run Django migration checks
6. Run tests
7. SSH into AWS EC2
8. Pull latest code
9. Rebuild Docker containers

---

## GitHub Secrets Required

```
EC2_HOST   → Public IP of server
EC2_USER   → ubuntu (or ec2-user)
EC2_KEY    → SSH private key
```

---

# 🔄 Deployment Command (Manual)

```bash
docker compose up -d --build
```

---

# 🧪 Health Check (Recommended)

Add endpoint:

```
/health/
```

Used for monitoring application status inside Traefik.

---

# 📊 Monitoring

## Traefik Dashboard

* Shows routing status
* Active services
* Request flow

## Logs

```bash
docker logs -f us-traefik-1
docker logs -f us-django-1
```

---

# ⚙️ Environment Variables

```env
POSTGRES_DB=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

# 🔐 Security Notes

* PostgreSQL is NOT exposed publicly
* Only Traefik is exposed externally
* SSH key-based authentication used for deployment
* Docker isolates services in internal network

---

# 📈 What This Project Demonstrates

✔ Production-grade backend architecture
✔ Reverse proxy routing (Traefik)
✔ Container orchestration (Docker Compose)
✔ Cloud deployment (AWS EC2)
✔ CI/CD automation (GitHub Actions)
✔ Real-world DevOps workflow

---

# 🚀 Future Improvements

* HTTPS with Let’s Encrypt (Traefik SSL)
* Domain name setup
* Blue-green deployment
* Auto rollback on failure
* Prometheus + Grafana monitoring
* Scaling with multiple Django instances

---

# 👨‍💻 Author

**Udith Sanadruwan**

* GitHub: udithsandaruwan2
* Portfolio: udithsandaruwan.me

---

# 📜 License

This project is for learning and educational DevOps practice.
