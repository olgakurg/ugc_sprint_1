from datetime import datetime

from pydantic import BaseModel


class Event(BaseModel):
    user_id: str
    event_time: datetime

    def get_key(self):
        return getattr(self, self.__key_field__)

    def get_value(self):
        value = {k: str(v) for k, v in self.dict().items() if v is not None}
        value["event_type"] = self.__class__.__name__
        return value


class MovieProgress(Event):
    __key_field__ = "movie_id"
    movie_id: str
    movie_progress: int
    movie_len: int


class MovieRes(Event):
    __key_field__ = "movie_id"
    movie_id: str
    old_res: str
    new_res: str


class ClickElement(Event):
    __key_field__ = "element_id"
    element_id: str


class FilterQuery(Event):
    __key_field__ = "user_id"
    query_param: str | None
    genre_id: str | None
    rating: str | None
    actor_id: str | None


class PageDuration(Event):
    __key_field__ = "page_id"
    page_id: str
    duration: int

