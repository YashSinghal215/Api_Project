# FastAPI Redis Rate Limiter (Sliding Window)

This project implements a configurable rate limiter using FastAPI and Redis.

It provides:
- One public API (no rate limit)
- One rate-limited API
- Sliding window rate limiting using Redis Sorted Sets (ZSET)
- Configurable time window and max request count

# Tech Stack

- Python 3.9+
- FastAPI
- Uvicorn
- Redis
  
# 1. Install Python Dependencies
pip install fastapi uvicorn redis pydantic-settings redis_client redis-cli

# 2. Install and Run Redis

- a. For  Windows:- (Need to have Ubuntu installed and use this in Ubuntu terminal)
  
  Install:
  
  sudo apt update
  sudo apt install redis-server
  
  Start:
  
  sudo service redis-server start
  
  Test:
  
  redis-cli ping
  
  Expected output:
  
  PONG

- b. For Mac
  
  Install:
  
  brew install redis
  
  Start Redis:
  
  brew services start redis
  
  Test:
  
  redis-cli ping
  
  Expected output:
  
  PONG

# 3. Run the FastAPI Application

From the project root directory:-

uvicorn app.main:app --reload

# 4. For API Endpoints
GET /limited

GET /public

Use curl command like example:

curl -H "X-User-Id: user1" http://127.0.0.1:8000/limited

curl -H "X-User-Id: user1" http://127.0.0.1:8000/public
