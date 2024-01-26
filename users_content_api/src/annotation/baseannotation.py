from typing import Annotated
from fastapi import Query, Body

from scheme.userscontent import InputContent


class AddUsersContent:
    def __init__(
        self,
        body: Annotated[
            InputContent,
            Body(
                examples=[
                    {
                        "relation_uuid": "e14b3ea9-b4db-4d73-a7d8-72815ac3eb61",
                        "access_token": "you access token",
                        "object_type": "comment",
                        "content": "my first comment"
                    }
                ],
            )
        ],
    ):
        self.body = body
