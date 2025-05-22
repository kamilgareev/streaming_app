from fastapi import FastAPI
from app.api.video import router

app = FastAPI()
app.include_router(router, prefix='/api/videos')
