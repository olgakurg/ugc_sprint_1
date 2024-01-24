from typing import Annotated
from fastapi import Query, Body

from scheme.userscontent import ContentObject


class AddUsersContent:
    def __init__(
        self,
        body: Annotated[
            ContentObject,
            Body(
                examples=[
                    {
                        "relation_uuid": "e14b3ea9-b4db-4d73-a7d8-72815ac3eb61",
                        "user_uuid": "e14b3ea9-b4db-4d73-a7d8-72815ac3eb61",
                        "object_type": "comment",
                        "content": "my first comment"
                    }
                ],
            )
        ],
    ):
        self.body = body
