
from http import HTTPStatus


test_auth = [
    (
        {'token_prefix': ""},
        {
            'status': HTTPStatus.CREATED,
            'detail': 'ok'
        }
    ),
    (
        {'token_prefix': "1"},
        {
            'status': HTTPStatus.BAD_REQUEST,
            'detail': 'Incorrect access token'
        }
    ),


]


test_created = [
    (
        {
            'input_data': {
                'relation_uuid': 'e14b3ea9-b4db-4d73-a7d8-72815ac3eb62',
                'access_token': None,
                'object_type': 'comment',
                'content': 'write_test'
            }
        },
        {
            'content': 'write_test',
            'status': HTTPStatus.CREATED,
        }
    ),

    (
        {
            'input_data': {
                'relationuuid': 'e14b3ea9-b4db-4d73-a7d8-72815ac3eb62',
                'access_token': None,
                'object_type': 'comment',
                'content': 'write_test'
            }
        },
        {
            'content': 'write_test',
            'status': HTTPStatus.UNPROCESSABLE_ENTITY
        }
    ),

    (
        {
            'input_data': {
                'relationuuid': 'e14b3ea9-b4db-4d73-a7d8-72815ac3eb62',
                'access_token': None,
                'objecttype': 'comment',
                'content': 'write_test'
            }
        },
        {
            'content': 'write_test',
            'status': HTTPStatus.UNPROCESSABLE_ENTITY
        }
    ),

    (
        {
            'input_data': {
                'relationuuid': 'e14b3ea9-b4db-4d73-a7d8-72815ac3eb62',
                'access_token': None,
                'object_type': 'comment',
                'contentss': 'write_test'
            }
        },
        {
            'content': 'write_test',
            'status': HTTPStatus.UNPROCESSABLE_ENTITY
        }
    ),

    (
        {
            'input_data': {
                'relationuuid': 'e14b3ea9-b4db-4d73-a7d8-72815ac3eb62',
                'access_token': None,
                'object_type': 'comment',
                'content': 'write_test',
                'event': 'like'
            }
        },
        {
            'content': 'write_test',
            'status': HTTPStatus.UNPROCESSABLE_ENTITY
        }
    ),


]
