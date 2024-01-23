from datetime import datetime

from pydantic import BaseModel


class Event(BaseModel):
    """
    Base Event model.
    """
    user_id: str
    event_time: datetime

    @property
    def key(self) -> str:
        """
        Returns the class name as the key.
        """
        return self.__class__.__name__

    @property
    def value(self) -> dict[str, str]:
        """
        Returns a dictionary of the model's fields and values.
        """
        return {k: str(v) for k, v in self.dict().items() if v is not None}


class MovieProgress(Event):
    """
    Event model for movie progress.
    """
    movie_id: str
    movie_progress: int
    movie_len: int


class MovieRes(Event):
    """
    Event model for movie resolution change.
    """
    movie_id: str
    old_res: str
    new_res: str


class ClickElement(Event):
    """
    Event model for element click.
    """
    element_id: str


class FilterQuery(Event):
    """
    Event model for filter query.
    """
    query_param: str | None = None
    genre_id: str | None = None
    rating: str | None = None
    actor_id: str | None = None


class PageDuration(Event):
    """
    Event model for page duration.
    """
    page_id: str
    duration: int
