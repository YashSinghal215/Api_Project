import time
from fastapi import Request, HTTPException
from redis_client import redis_client
from config import settings


async def rate_limiter(request: Request):
    user_id = request.headers.get("X-User-Id")
    if not user_id:
        raise HTTPException(status_code=400, detail="X-User-Id header required")

    key = f"rate_limit:{user_id}"

    current_time = int(time.time() * 1000)
    window_start = current_time - (settings.RATE_LIMIT_WINDOW * 1000)

    try:
        # Remove expired requests
        redis_client.zremrangebyscore(key, 0, window_start)

        # Get current request count
        request_count = redis_client.zcard(key)

        if request_count >= settings.RATE_LIMIT_MAX:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded"
            )

        # Add current request timestamp
        redis_client.zadd(key, {str(current_time): current_time})

        # Set expiry
        redis_client.expire(key, settings.RATE_LIMIT_WINDOW)

        return True
    except HTTPException:
        raise
    except Exception as e:
        print("Redis error:", e)
        raise HTTPException(status_code=500, detail="Redis error")