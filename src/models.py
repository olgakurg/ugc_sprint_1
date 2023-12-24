from datetime import datetime

from pydantic import BaseModel


class MovieProgress(BaseModel):
    user_id: str
    event_time: datetime
    movie_id: str
    movie_progress: int
    movie_len: int


class MovieRes(BaseModel):
    user_id: str
    event_time: datetime
    movie_id: str
    old_res: str
    new_res: str


class ClickElement(BaseModel):
    user_id: str
    event_time: datetime
    element_id: str


class FilterQuery(BaseModel):
    user_id: str
    event_time: datetime
    query_param: str | None
    genre_id: str | None
    rating: str | None
    actor_id: str | None


class PageDuration(BaseModel):
    user_id: str
    event_time: datetime
    page_id: str
    duration: int
