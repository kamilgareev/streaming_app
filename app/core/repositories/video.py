from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.connection import db_connection
from app.core.db.models import Video


class VideoRepository:

    @staticmethod
    @db_connection
    async def create(title: str, url: str, session: AsyncSession):
        video = Video(title=title, url=url)
        session.add(video)
        await session.commit()
        return video
