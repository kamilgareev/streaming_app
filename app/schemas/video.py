from pydantic import BaseModel, HttpUrl


class VideoCreate(BaseModel):
    title: str
    url: HttpUrl


class VideoResponse(BaseModel):
    id: int
    title: str
    playlist_url: HttpUrl
