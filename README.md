# 🚀 **Enterprise Asset Tracking System (EATS)**

**A high-performance, modular Django application designed for precision tracking of assets and their movements across complex logistical environments.**

Engineered as a foundational element for modern supply-chain and asset management platforms, this system prioritizes **speed, scalability, and operational clarity** through optimized database practices, advanced caching strategies, and comprehensive monitoring.

## 🏷️ **Badges**

![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
![Django Version](https://img.shields.io/badge/django-5.2.8-green.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-15-blue.svg)
![Redis](https://img.shields.io/badge/redis-7-red.svg)
![CI](https://github.com/<your-org-or-user>/<repo>/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ **Core Stack & Architecture**

| Component | Technology | Version/Description |
| :--- | :--- | :--- |
| **Backend Framework** | **[Django](https://www.djangoproject.com/)** | **5.2.8** (LTS-ready) |
| **Programming Language** | **[Python](https://www.python.org/)** | **3.11+** |
| **Primary Database** | **[PostgreSQL](https://www.postgresql.org/)** | Optimized for relational integrity and query performance. |
| **High-Speed Cache** | **[Redis](https://redis.io/)** (via `django-redis`) | **7** – Used for session, data, and view caching. |
| **Continuous Integration** | **[GitHub Actions](https://github.com/features/actions)** | Automated testing and quality gate enforcement. |
| **Linting** | **[Flake8](https://flake8.pycqa.org/)** | Enforces code quality and style standards. |

---

## 💎 **Key Features & Performance Differentiators**

* **Holistic CRUD Management:** Comprehensive operations for **Assets**, **Locations**, and **Asset Movement** records, ensuring full data lifecycle control.
* **Performance Engineering:** Achieved through meticulous **Query Optimization** (leveraging `select_related`, `prefetch_related`, and database aggregates) to minimize database load and latency.
* **Scalable Caching:** **Redis-backed Caching** implementation for improved response times, with strategic **View-Level Caching** (e.g., Dashboard cached for 60 seconds) to reduce computational overhead.
* **Proactive System Monitoring:** Integrated **Prometheus-style metrics endpoint** (`/assets/metrics/`) providing real-time visibility into:
    * Cache Performance (Hit/Miss Ratio).
    * Application Response Times (Avg, Median, P95).
    * System Health and Resource Utilization.
* **Secure Access Control:** Robust **Role-Based Permissions** built upon Django's native authentication system to govern data access and operational capabilities.
* **Aggregated Analytics:** A centralized **Dashboard** providing aggregated metrics and actionable insights from real-time operational data.

---

## 📂 **Project Structure Overview**

The modular structure promotes maintainability and scalability, separating core concerns into logical Django applications and configuration files.

---

## 🌐 **RESTful API Endpoints**

The application exposes a set of clear, resource-oriented endpoints for integration with external services and frontends.

| Resource | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **Assets** | `GET` | `/assets/` | Retrieve a filtered list of assets. |
| | `POST` | `/assets/create/` | Provision a new asset record. |
| | `GET/POST` | `/assets/<id>/...` | Retrieve, update, or delete a specific asset. |
| **Locations** | `GET` | `/locations/` | List and search all storage and transit locations. |
| | `POST` | `/locations/create/` | Register a new operational location. |
| **Movements** | `GET` | `/movements/` | View historical and in-transit movement logs. |
| | `POST` | `/movements/create/` | Record a transfer event (e.g., Check-out, Transfer). |
| **Monitoring** | `GET` | `/assets/metrics/` | Fetch Prometheus-compatible system health metrics (JSON). |
| **Dashboard** | `GET` | `/` | Main analytical dashboard (cached). |

---

## 🛠️ **Quick Start Guide**

### **Prerequisites**

* **Python** 3.11+
* **PostgreSQL** (Active local or remote instance)
* **Redis** (Required for enabling high-speed caching)

### **Installation**

1.  **Setup Environment:**
    ```bash
    git clone <repository-url>
    cd asset-tracking
    python -m venv venv
    source venv/bin/activate
    ```

2.  **Dependencies & Database Setup:**
    ```bash
    pip install -r requirements.txt
    # Ensure PostgreSQL is configured in settings.py
    python manage.py migrate
    python manage.py createsuperuser
    ```

3.  **Optional: Enable Redis Caching**
    For optimal performance, start Redis (e.g., via Docker) and set the environment variable:
    ```bash
    docker run -p 6379:6379 --name redis -d redis:7
    export REDIS_URL='redis://127.0.0.1:6379/1'
    ```

4.  **Run Development Server:**
    ```bash
    python manage.py runserver
    # Access: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    ```

---

## 🧪 **Testing Strategy**

A commitment to code quality is enforced via a comprehensive test suite covering functionality, security, and performance.

| Test Category | Description | Execution |
| :--- | :--- | :--- |
| **Unit & Integration** | Covers models, views, and core business logic. | `python manage.py test` |
| **Caching Tests** | Validates Redis interaction and cache eviction policies. | `python manage.py test assets.test_caching` |
| **Security Tests** | Verifies role-based access control and authentication flows. | `python manage.py test assets.test_permissions` |

To run tests with code coverage:
```bash
pip install coverage
coverage run manage.py test
coverage report

🤝 Contributing to EATS
We welcome contributions to enhance the system's robustness and feature set.

Fork the repository and clone your fork.

Create a descriptive feature branch (git checkout -b feat/add-api-versioning).

Implement your changes, adhering to PEP 8 and established design patterns.

Crucially, add or update tests to ensure full coverage of new logic.

Ensure all CI checks (tests, linting) pass locally.

Open a Pull Request with a clear title and description of the changes.

Roadmap & Future Enhancements
[ ] API Versioning: Implement a structured versioning strategy (e.g., /api/v1/assets/).

[ ] Real-Time Notifications: Integrate WebSockets (e.g., Django Channels) for instant movement alerts.

[ ] Advanced Data Export: Add robust export functionalities (CSV, PDF, Excel) for reporting.

[ ] Analytics Module: Develop sophisticated reporting views and predictive analytics tools.

License
This project is open-sourced under the MIT License.
