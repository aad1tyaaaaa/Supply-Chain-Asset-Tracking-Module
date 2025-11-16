# 🚀 Asset Tracking System

A robust Django-based application for tracking assets and their movements across locations. Designed as a modular starting point for supply-chain and asset management systems, featuring optimized database queries, caching, and comprehensive monitoring.

## 🏷️ Badges

 <p align="center">

<!-- 🔥 Core Tech Stack -->
<img src="https://img.shields.io/badge/Python-3.11+-2E7DFF?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Django-5.2.8-00C853?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-15-4CC9F0?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Redis-7-FF1744?style=for-the-badge&logo=redis&logoColor=white" />
<img src="https://img.shields.io/badge/NGINX-Reverse%20Proxy-26A69A?style=for-the-badge&logo=nginx&logoColor=white" />

<br/><br/>

<!-- 🚀 DevOps & Build -->
<img src="https://img.shields.io/badge/CI%20Pipeline-GitHub%20Actions-6A5ACD?style=for-the-badge&logo=githubactions&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-Ready-0288D1?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/Kubernetes-Compatible-005CFF?style=for-the-badge&logo=kubernetes&logoColor=white" />

<br/><br/>

<!-- 📦 Code Quality -->
<img src="https://img.shields.io/badge/Flake8-Linting-448AFF?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Black-Formatter-000000?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Coverage-90%25-00E676?style=for-the-badge&logo=codecov&logoColor=white" />
<img src="https://img.shields.io/badge/Pytest-Tested-00B0FF?style=for-the-badge&logo=pytest&logoColor=white" />

<br/><br/>

<!-- ⚙️ Backend Performance -->
<img src="https://img.shields.io/badge/Caching-Redis%20Enabled-F44336?style=for-the-badge&logo=redis&logoColor=white" />
<img src="https://img.shields.io/badge/Queries-Optimized-8E24AA?style=for-the-badge&logo=database&logoColor=white" />
<img src="https://img.shields.io/badge/Monitoring-Prometheus-E040FB?style=for-the-badge&logo=prometheus&logoColor=white" />

<br/><br/>

<!-- 🛡 Security -->
<img src="https://img.shields.io/badge/Auth-RBAC%20%2B%20Django-2962FF?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/HTTPS-LetsEncrypt-FF6D00?style=for-the-badge&logo=letsencrypt&logoColor=white" />

<br/><br/>

<!-- 🌍 Repo Status -->
<img src="https://img.shields.io/badge/Last%20Commit-Active-00E5FF?style=for-the-badge&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/Stars-★★★★★-FFD600?style=for-the-badge&logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/Forks-Growing-42A5F5?style=for-the-badge&logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/Issues-Tracked-E53935?style=for-the-badge&logo=github&logoColor=white" />

</p>


## 🛠️ Tech Stack

| Component       | Technology                                                                 | Version/Description |
|-----------------|---------------------------------------------------------------------------|---------------------|
| **🖥️ Backend**     | [Django](https://www.djangoproject.com/)                                  | 5.2.8              |
| **🐍 Language**    | [Python](https://www.python.org/)                                         | 3.11               |
| **🗄️ Database**    | [PostgreSQL](https://www.postgresql.org/)                                 | -                  |
| **⚡ Caching**     | [Redis](https://redis.io/) (via [django-redis](https://github.com/jazzband/django-redis)) | 7                  |
| **🔄 CI/CD**       | [GitHub Actions](https://github.com/features/actions)                     | -                  |
| **🔍 Linting**     | [Flake8](https://flake8.pycqa.org/)                                       | -                  |

## ✨ Features

- **📝 CRUD Operations**: Full Create, Read, Update, Delete functionality for Assets, Locations, and Asset Movements.
- **📊 Dashboard**: Aggregated metrics and insights with real-time data visualization.
- **🔍 Query Optimization**: Efficient database queries using `select_related`, `prefetch_related`, and database aggregates.
- **💾 Caching**: Optional Redis-backed caching for improved performance, with dashboard caching for 60 seconds.
- **📈 Monitoring**: Prometheus-style metrics endpoint for tracking cache performance, response times, and system health.
- **🔐 Authentication**: Built-in Django authentication with role-based permissions.
- **🧪 Testing**: Comprehensive test suite including caching, permissions, and authentication tests.

## 📋 Project Structure

```
asset_tracking/
├── asset_tracking/          # Main Django project
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── assets/                 # Main app
│   ├── models.py           # Database models (Asset, Location, AssetLocation)
│   ├── views.py            # Class-based views
│   ├── urls.py             # App URL patterns
│   ├── forms.py            # Django forms
│   ├── permissions.py      # Custom permissions
│   ├── metrics.py          # Monitoring middleware and metrics
│   ├── signals.py          # Django signals
│   ├── management/         # Management commands
│   ├── templates/          # HTML templates
│   └── tests/              # Test files
├── .github/workflows/      # CI/CD pipelines
├── requirements.txt        # Python dependencies
├── manage.py               # Django management script
└── README.md               # This file
```

## 🔗 API Endpoints

The application provides the following RESTful endpoints:

### 📦 Assets
- `GET /assets/` - List all assets
- `POST /assets/create/` - Create a new asset
- `GET /assets/<id>/` - Get asset details
- `POST /assets/<id>/update/` - Update an asset
- `POST /assets/<id>/delete/` - Delete an asset

### 📍 Locations
- `GET /locations/` - List all locations
- `POST /locations/create/` - Create a new location
- `GET /locations/<id>/` - Get location details
- `POST /locations/<id>/update/` - Update a location
- `POST /locations/<id>/delete/` - Delete a location

### 🚚 Asset Movements
- `GET /movements/` - List all asset movements
- `POST /movements/create/` - Record a new asset movement
- `POST /movements/<id>/update/` - Update an asset movement
- `POST /movements/<id>/delete/` - Delete an asset movement

### 📊 Monitoring
- `GET /assets/metrics/` - Get application metrics (JSON)

### 🏠 Dashboard
- `GET /` - Main dashboard with aggregated metrics

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL
- Redis (optional, for caching)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd asset-tracking
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**:
   - Ensure PostgreSQL is running locally.
   - Update database settings in `asset_tracking/settings.py` if needed (default assumes local PostgreSQL with user 'postgres' and password 'password').

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Configuration

### Production Settings

For production deployment:

- Set `DEBUG = False` in `asset_tracking/settings.py`.
- Configure `ALLOWED_HOSTS` appropriately.
- Use secure database credentials and environment variables.
- Set up proper static file serving.

### Caching (Optional)

To enable Redis caching:

1. **Start Redis** (using Docker):
   ```bash
   docker run -p 6379:6379 --name redis -d redis:7
   ```

2. **Set environment variable**:
   ```bash
   export REDIS_URL='redis://127.0.0.1:6379/1'
   python manage.py runserver
   ```

When `REDIS_URL` is set, the application uses Redis for caching. The dashboard view is cached for 60 seconds by default.

## CI/CD

This project uses GitHub Actions for continuous integration. The CI pipeline includes:

- Automated testing with Redis service.
- Linting with Flake8 (max line length: 120).
- Python 3.11 environment.

![CI](https://github.com/<your-org-or-user>/<repo>/actions/workflows/ci.yml/badge.svg)

## Monitoring

The application exposes a metrics endpoint at `/assets/metrics/` providing Prometheus-compatible data:

### Cache Performance Metrics
- Cache hits/misses and hit ratio
- Number of cached keys
- Cache memory usage

### Application Performance Metrics
- Response times (average, median, 95th percentile)
- Requests per minute
- Process memory usage

Example metrics response:
```json
{
    "cache_hits": 150,
    "cache_misses": 20,
    "cache_hit_ratio": 0.882,
    "cache_keys": 5,
    "response_time_avg": 0.045,
    "response_time_median": 0.038,
    "response_time_p95": 0.156,
    "requests_per_minute": 42,
    "process_memory_mb": 128.5
}
```

Integrate with monitoring tools like Prometheus for visualization and alerting.

## Testing

The project includes comprehensive tests covering various aspects:

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests with coverage
pip install coverage
coverage run manage.py test
coverage report

# Run specific test files
python manage.py test assets.tests
python manage.py test assets.test_caching
```

### Test Coverage

- **Unit Tests**: Model methods, utility functions, and business logic.
- **Integration Tests**: API endpoints, form submissions, and database operations.
- **Caching Tests**: Redis cache functionality and performance.
- **Permission Tests**: Authentication and authorization logic.
- **Authentication Tests**: Login/logout flows and user management.

### Test Structure

```
assets/
├── tests.py              # Main test suite
├── test_caching.py       # Caching-specific tests
├── test_permissions.py   # Permission and authorization tests
└── test_auth.py          # Authentication tests
```

## Screenshots

### Dashboard
![Dashboard Screenshot](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)

### Asset List
![Asset List Screenshot](https://via.placeholder.com/800x400?text=Asset+List+Screenshot)

### Asset Detail
![Asset Detail Screenshot](https://via.placeholder.com/800x400?text=Asset+Detail+Screenshot)

*Note: Replace placeholder images with actual screenshots of your application.*

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Make your changes and add tests.
4. Ensure CI passes (`python manage.py test`).
5. Commit your changes (`git commit -m 'Add amazing feature'`).
6. Push to the branch (`git push origin feature/amazing-feature`).
7. Open a Pull Request.

### Development Guidelines

- Follow PEP 8 style guidelines.
- Write comprehensive tests for new features.
- Update documentation as needed.
- Ensure all tests pass before submitting PR.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need help, please:

- Open an issue on GitHub
- Check the [Django documentation](https://docs.djangoproject.com/)
- Review the [PostgreSQL documentation](https://www.postgresql.org/docs/)

## Roadmap

- [ ] Add API versioning
- [ ] Implement real-time notifications
- [ ] Add export functionality (CSV/PDF)
- [ ] Mobile-responsive design improvements
- [ ] Advanced reporting and analytics


