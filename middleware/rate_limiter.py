import time
from fastapi import Request, HTTPException
from redis_client import redis_client


async def rate_limiter(
    request: Request,
    user_id: str,
    time_window: int,
    max_count: int
):
    if not user_id:
        raise HTTPException(status_code=400, detail="userId is required")

    key = f"rate_limit:{user_id}"
    print("hello")
    try:
        current_count = redis_client.incr(key)
        print(current_count)
        if current_count == 1:
            redis_client.expire(key, time_window)

        if current_count > max_count:
            raise HTTPException(
                status_code=429,
                detail=f"Rate limit exceeded. Max {max_count} requests in {time_window} seconds."
            )

    except Exception:
        raise HTTPException(status_code=500, detail="Rate limiter error")