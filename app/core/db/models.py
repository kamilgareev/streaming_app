from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db.base import Base


class Video(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str]
    url: Mapped[str]
