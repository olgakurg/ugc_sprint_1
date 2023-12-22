from datetime import datetime

from pydantic import BaseModel


class Instance(BaseModel):
    user_id: str
    event_time: datetime


class Movie(Instance):
    movie_id: str


class MovieProgress(BaseModel):
    user_id: str
    event_time: datetime
    movie_id: str
    movie_progress: int
    movie_len: int


class MovieResolution(Movie):
    old_res: str
    new_res: str
