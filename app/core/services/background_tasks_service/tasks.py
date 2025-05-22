import logging

from app.core.services.background_tasks_service.celery import celery_app
from app.core.services.background_tasks_service.logic import generate_hls_playlist, cache_hls_playlist, cache_video

logger = logging.getLogger(__name__)


@celery_app.task
def process_video(video_id: int, video_title: str, playlist_url: str) -> None:
    try:
        hls_playlist = generate_hls_playlist(video_id)
        cache_hls_playlist(playlist_url, hls_playlist)
        cache_video(video_id, video_title, playlist_url)
    except Exception as e:
        logger.error(f'Error occurred while processing video {video_title},'
                     f'details: {e}')
        raise
