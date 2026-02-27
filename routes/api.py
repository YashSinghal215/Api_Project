from fastapi import APIRouter, Request, Query
from middleware.rate_limiter import rate_limiter

router = APIRouter()

@router.get("/public")
async def public_api():
    return {"message": "This API has no rate limiting"}


@router.get("/limited")
async def limited(request: Request):
    await rate_limiter(request)
    return {"message": "Rate limited API working"}