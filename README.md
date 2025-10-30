# FastAPI CRUD API with Image Upload

A **lightweight, database-free** FastAPI backend for managing products with **image upload**, **in-memory + JSON persistence**, and **Docker support**.

Perfect for **prototypes, demos, or small apps**.

---

## Features

| Feature               | Status |
|-----------------------|--------|
| Create / Read / Update / Delete | Yes |
| Image Upload + Serve  | Yes |
| UUID-based IDs        | Yes |
| JSON file persistence (`data/items.json`) | Yes |
| Dockerized            | Yes |
| Deployable to Render, Railway, Fly.io | Yes |

---


## Quick Start (Local)

```bash
# 1. Clone repo
git clone https://github.com/hakvenlong/fastapi.git
cd fastapi

# 2. Install
pip install -r requirements.txt

# 3. Run
uvicorn main:app --reload

# Build
docker build -t fastapi-crud .

# Run
docker run -p 8000:8000 fastapi-crud
