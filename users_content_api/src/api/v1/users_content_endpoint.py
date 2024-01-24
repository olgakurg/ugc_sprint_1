from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from annotation.baseannotation import AddUsersContent
from services.userstorage import UserStoregeService, get_user_storage_service
from scheme.userscontent import CreateResponse, CountResponse, AvgResponse, ContentObjectsResponse

router = APIRouter()


@router.post(
    '/create',
    response_model=CreateResponse,
    status_code=HTTPStatus.CREATED
)
async def add_content(
    common: AddUsersContent = Depends(AddUsersContent),
    user_content_storage: UserStoregeService = Depends(
        get_user_storage_service)
):
    content = await user_content_storage.add_content(common.body)

    if not content:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail="can't add this content"
        )

    return {
        'status': "ok",
        '_id': str(content.inserted_ids[0])
    }


@router.get(
    '/count',
    response_model=CountResponse,
    status_code=HTTPStatus.CREATED
)
async def get_count(
    object_type: str,
    relation_uuid: str = None,
    user_content_storage: UserStoregeService = Depends(
        get_user_storage_service)
):
    content = await user_content_storage.get_count(
        'object_type',
        object_type,
        relation_uuid
    )

    if not content:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail="can't add this content"
        )

    return {
        'count': content
    }


@router.get(
    '/avg_rating',
    response_model=AvgResponse,
    status_code=HTTPStatus.CREATED
)
async def get_ratting(
    movie_uuid: str,
    user_content_storage: UserStoregeService = Depends(
        get_user_storage_service)
):
    ratting = await user_content_storage.get_avg_rating(movie_uuid)

    if not ratting:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail="can't add this content"
        )

    return {
        'result': ratting
    }


@router.get(
    '/objects',
    response_model=ContentObjectsResponse,
    status_code=HTTPStatus.CREATED
)
async def get_objects(
    object_id: str,
    object_type: str,
    user_content_storage: UserStoregeService = Depends(
        get_user_storage_service)
):
    objects = await user_content_storage.get_objects(object_id, object_type)

    if not objects:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail="can't add this content"
        )

    return {'content': objects}
