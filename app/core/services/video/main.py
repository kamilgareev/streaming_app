from app.core.repositories.video import VideoRepository as VideoRepo
from app.core.services.background_tasks_service.redis import redis_client
from app.core.services.background_tasks_service.tasks import process_video


class VideoService:
    @staticmethod
    async def retrieve(video_id: int):
        return redis_client.hgetall(f'video_{video_id}')

    @staticmethod
    async def create(title: str, url: str):
        video = await VideoRepo.create(title=title, url=url)
        # для примера
        playlist_url = f'https://example.com/hls/{video.id}.m3u8'
        process_video.delay(
            video_id=video.id,
            video_title=video.title,
            playlist_url=playlist_url
        )
        return video, playlist_url
