from typing import List
from time import time


from pydantic import Field, BaseModel


class ContentObject(BaseModel):
    """
    model descripted users content data

    """
    relation_uuid: str
    user_uuid: str
    object_type: str
    timestamp: float = time()
    content: str | int = Field(None)


class CreateResponse(BaseModel):
    """
    model descripted respons for post method

    """
    status: str
    _id: str


class CountResponse(BaseModel):
    """
    model descripted respons for counts

    """
    count: int


class AvgResponse(BaseModel):
    """
    model descripted respons for avg func

    """
    result: float


class ContentObjectsResponse(BaseModel):
    content: list[ContentObject]
