import uuid

from fastapi import Depends

from db.store import BaseStorage
from db.mongosrore import Mongo
from scheme.userscontent import ContentObject
from core.config import settings


class UserStoregeService:
    def __init__(self, db: BaseStorage):
        self.db = db

    async def add_content(
        self,
        content: ContentObject
    ) -> dict:
        result = await self.db.async_write(
            settings.uc_collections,
            [content.model_dump()]
        )

        return result

    async def get_count(self, object_type, value, relation_uuid) -> int:
        result = await self.db.async_count(
            settings.uc_collections,
            object_type,
            value,
            relation_uuid
        )
        return result

    async def get_avg_rating(self, movie_uuid: str) -> float:

        pipline = [
            {
                '$match': {
                    'relation_uuid': movie_uuid,
                    'object_type': 'rating'
                }
            },
            {
                '$group': {
                    '_id': 'null',
                    'avg': {'$avg': '$content'}
                }

            }
        ]

        result = await self.db.async_aggregate_func(
            settings.uc_collections,
            pipline

        )

        return result[0]['avg'] if result else None

    async def get_objects(self, object, object_type):
        pipline = [
            {
                '$match': {
                    'relation_uuid': object,
                    'object_type': object_type,
                }
            },
        ]

        objects = await self.db.async_aggregate_func(
            settings.uc_collections,
            pipline

        )

        for object in objects:
            object['_id'] = str(object['_id'])

        return objects


def get_user_storage_service() -> UserStoregeService:

    storage = Mongo(
        settings.uc_host,
        settings.uc_port,
        settings.uc_database
    )

    return UserStoregeService(storage)
