import redis

from app.core.config import settings

redis_client = redis.from_url(
    url=settings.redis.CACHE_URL,
    decode_responses=True
)
