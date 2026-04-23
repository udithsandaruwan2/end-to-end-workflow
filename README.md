# 🚀 Django API with Traefik Reverse Proxy (Dockerized)

A production-ready backend setup using **Django**, **PostgreSQL**, **Docker**, and **Traefik** as a reverse proxy with service discovery.

---

## 📌 Overview

This project demonstrates a modern backend architecture:

* Django REST API (served via Gunicorn)
* PostgreSQL database
* Traefik reverse proxy for routing
* Dockerized services using Docker Compose

---

## 🏗️ Architecture

```
Browser (localhost:8081)
        ↓
     Traefik (Port 80 inside container)
        ↓
     Django (Gunicorn - Port 8000)
        ↓
     PostgreSQL (Port 5432)
```

---

## ⚙️ Tech Stack

* Python (Django)
* Gunicorn
* PostgreSQL
* Docker & Docker Compose
* Traefik (Reverse Proxy & Load Balancer)

---

## 📁 Project Structure

```
.
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── config/
├── app/
├── requirements / pyproject.toml (uv)
└── ...
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

### 2️⃣ Build and run the containers

```bash
docker compose up -d --build
```

---

### 3️⃣ Access the application

* 🌐 Django API:
  http://localhost:8081/

* ⚙️ Traefik Dashboard:
  http://localhost:8080/dashboard/

---

## 🔐 Environment Variables

Configured inside `docker-compose.yml`:

```yaml
POSTGRES_DB=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

## 🧪 Running Migrations

```bash
docker exec -it <django-container> python manage.py migrate
```

---

## 👤 Create Superuser

```bash
docker exec -it <django-container> python manage.py createsuperuser
```

Access admin panel:

```
http://localhost:8081/admin/
```

---

## 🔄 Traefik Routing

Routing is handled using Docker labels:

```yaml
- "traefik.enable=true"
- "traefik.http.routers.django.rule=PathPrefix(`/`)"
- "traefik.http.routers.django.entrypoints=web"
- "traefik.http.services.django.loadbalancer.server.port=8000"
```

---

## 📊 Monitoring

### Traefik Dashboard

* View routers, services, and status
* URL: http://localhost:8080/dashboard/

### Enable Access Logs (optional)

```yaml
--accesslog=true
--log.level=INFO
```

---

## ❤️ Health Check (Recommended)

Add a health endpoint in Django:

```python
def health_check(request):
    return JsonResponse({"status": "ok"})
```

Then configure Traefik:

```yaml
- "traefik.http.services.django.loadbalancer.healthcheck.path=/health/"
```

---

## 🐳 Docker Commands

### Stop containers

```bash
docker compose down
```

### Rebuild

```bash
docker compose up -d --build
```

### View logs

```bash
docker logs -f us-django-1
docker logs -f us-traefik-1
```

---

## 🔥 Future Improvements

* HTTPS with Let’s Encrypt
* Domain-based routing
* CI/CD pipeline (GitHub Actions)
* Load balancing multiple Django instances
* Monitoring with Prometheus & Grafana

---

## ⚠️ Notes

* Traefik handles all incoming traffic (no direct Django exposure)
* PostgreSQL is isolated within Docker network
* Port 8081 is used only for development

---

## 👨‍💻 Author

Udith Sandaruwan

* GitHub: udithsandaruwan2
* Portfolio: udithsandaruwan.me

---

## 📜 License

This project is for educational and development purposes.
