from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "celery_worker",
    broker=settings.redis.CELERY_BROKER_URL,
    backend=settings.redis.CELERY_RESULT_BACKEND_URL
)