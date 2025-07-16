# Trade Analysis Platform

This project is a dual-framework web application combining:
- **FastAPI** for market opportunity analysis APIs (`trade_api`)
- **Django** for admin dashboard and frontend management (`trade_project`)

The services are containerized using Docker for easy deployment and scalability.

---

## 🐳 Getting Started with Docker

### Prerequisites

- Docker & Docker Compose installed
- Python 3.10+ (for local dev testing)

### 🔧 Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/trade-analysis-platform.git
   cd trade-analysis-platform
   ```

2. **Add your `.env` file in `trade_api/.env` with API keys or secrets.**

3. **Build and run the containers:**

   ```bash
   docker-compose up --build
   ```

   - Django will be served at: `http://localhost:8000/`
   - FastAPI docs available at: `http://localhost:8001/docs`

4. **Stop containers:**

   ```bash
   docker-compose down
   ```

---

## 🧾 Project Structure

```
.
├── docker-compose.yml       # Defines Django and FastAPI services
├── Dockerfile               # Shared Dockerfile
├── requirements.txt         # Base requirements (used for Docker build)
│
├── trade_api/               # FastAPI app
│   ├── app/                 # Core FastAPI logic
│   └── tests/               # Test cases
│
└── trade_project/           # Django app
    ├── frontend/            # Django frontend app
    └── trade_project/       # Django core project files
```
