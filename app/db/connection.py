from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import settings

engine = create_async_engine(url=settings.db.DB_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


def db_connection(method):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                return await method(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()

    return wrapper
