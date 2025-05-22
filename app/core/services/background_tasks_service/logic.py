import logging

from app.core.services.background_tasks_service.redis import redis_client

logger = logging.getLogger(__name__)


def generate_hls_playlist(video_id: int) -> str:
    logger.info(f'Started generating HLS-playlist for video_id {video_id}')

    # просто для примера
    target_duration = 10
    media_sequence = 0
    num_segments = 3

    hls_content_lines = [
        '#EXTM3U',
        f'#EXT-X-VERSION:3',
        f'#EXT-X-TARGETDURATION:{target_duration}',
        f'#EXT-X-MEDIA-SEQUENCE:{media_sequence}',
    ]

    for i in range(num_segments):
        segment_duration = 10.0
        segment_name = f'example_segment_video_{video_id}_{i}.ts'
        hls_content_lines.append(f'#EXTINF:{segment_duration:.1f},')
        hls_content_lines.append(segment_name)

    hls_content_lines.append('#EXT-X-ENDLIST')
    hls_playlist_content = '\n'.join(hls_content_lines)

    logger.info(f'HLS-playlist for video_id {video_id} has been generated successfully')
    return hls_playlist_content


def cache_hls_playlist(playlist_url: str, playlist_content) -> None:
    logger.info(f'Started caching {playlist_url} content')
    redis_client.set(playlist_url, playlist_content)
    logger.info(f'Playlist {playlist_url} content has been cached successfully')


def cache_video(video_id: int, video_title: str, playlist_url: str) -> None:
    logger.info(f'Started caching {video_title} video')
    key = f'video_{video_id}'
    mapping = {
        'id': video_id,
        'title': video_title,
        'playlist_url': playlist_url
    }
    redis_client.hset(name=key, mapping=mapping)
    logger.info(f'Video {video_title} has been cached successfully')
