from fastapi import FastAPI
from routes.api import router

app = FastAPI(title="Configurable Redis Rate Limiter")

app.include_router(router)