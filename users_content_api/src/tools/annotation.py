from typing import Annotated

from fastapi import Query


class PaginationAnnotated:

    def __init__(
        self,
        page_number: Annotated[int, Query(
            description='page number', ge=0)] = 0,
        page_size: Annotated[int, Query(
            description='size of page', ge=1, le=100)] = 50,
    ):
        self.page_number = page_number
        self.page_size = page_size
