from fastapi import APIRouter, Request, Query
from middleware.rate_limiter import rate_limiter

router = APIRouter()

@router.get("/public")
async def public_api():
    return {"message": "This API has no rate limiting"}


@router.get("/limited")
async def limited_api(
    request: Request,
    userId: str = Query(...),
    time: int = Query(..., description="Time window in seconds"),
    maxCount: int = Query(..., description="Max requests allowed")
):
    await rate_limiter(request, userId, time, maxCount)
    return {"message": "This API is rate limited"}