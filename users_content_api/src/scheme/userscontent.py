from typing import List
from time import time


from pydantic import Field, BaseModel


class Content(BaseModel):
    """
    model describes users input content 

    """
    relation_uuid: str
    object_type: str
    timestamp: float = time()
    content: str | int = Field(None)


class InputContent(Content):
    """
    model describes users input content 

    """
    access_token: str


class ContentObject(Content):
    """
    model describes users content data

    """
    user_uuid: str


class CreateResponse(BaseModel):
    """
    model describes respons for post method

    """
    detail: str
    _id: str


class CountResponse(BaseModel):
    """
    model describes respons for counts

    """
    count: int


class AvgResponse(BaseModel):
    """
    model describes respons for avg func

    """
    result: float


class ContentObjectsResponse(BaseModel):
    content: list[ContentObject]
