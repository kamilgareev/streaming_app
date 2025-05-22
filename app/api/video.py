import logging

from fastapi import APIRouter, HTTPException, status

from app.schemas.video import VideoCreate, VideoResponse
from app.core.services.video import VideoService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post('/', response_model=VideoResponse, status_code=status.HTTP_201_CREATED)
async def create_video_endpoint(video: VideoCreate):
    try:
        video, playlist_url = await VideoService.create(title=video.title, url=str(video.url))
        return VideoResponse(
            id=video.id,
            title=video.title,
            playlist_url=playlist_url
        )
    except Exception as e:
        logger.error(f'Error creating video, details: {e}')
        raise HTTPException(
            status_code=500,
            detail='Unexpected error occurred'
        )


@router.get('/{video_id}/', response_model=VideoResponse)
async def retrieve_video_endpoint(video_id: int):
    try:
        video_data = await VideoService.retrieve(video_id=video_id)
        if not video_data:
            raise HTTPException(
                status_code=404,
                detail='Video not found'
            )
        return VideoResponse(**video_data)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f'Error retrieving video {video_id}, details: {e}')
        raise HTTPException(
            status_code=500,
            detail='Unexpected error occurred'
        )
