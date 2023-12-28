from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Event(BaseModel):
    user_id: str
    event_time: datetime

    @property
    def key(self):
        return self.__class__.__name__

    @property
    def value(self):
        return {k: str(v) for k, v in self.dict().items() if v is not None}


class MovieProgress(Event):
    movie_id: str
    movie_progress: int
    movie_len: int


class MovieRes(Event):
    movie_id: str
    old_res: str
    new_res: str


class ClickElement(Event):
    element_id: str


class FilterQuery(Event):
    query_param: Optional[str] = None
    genre_id: Optional[str] = None
    rating: Optional[str] = None
    actor_id: Optional[str] = None


class PageDuration(Event):
    page_id: str
    duration: int

