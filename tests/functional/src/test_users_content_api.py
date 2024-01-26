import pytest
from http import HTTPStatus
import time

from utils.url_constuctor import url_constructor
from testdata.users_content import test_auth, test_created
from testdata.user_content_generator import test_metrics


class TestUCApi:

    @pytest.mark.parametrize(
        'query_data, expected_answer',
        test_auth

    )
    @pytest.mark.asyncio
    async def test_auth(
        self, query_data, expected_answer, make_request, get_access
    ):

        url = url_constructor('user_content/create')

        access_token = get_access() + query_data['token_prefix']

        user_params = {
            "relation_uuid": "e14b3ea9-b4db-4d73-a7d8-72815ac3eb61",
            "access_token": access_token,
            "object_type": "comment",
            "content": "my first comment"
        }

        reg_response = await make_request('post', url, params=user_params)

        res = await reg_response.json(content_type=None)

        assert reg_response.status == expected_answer['status']
        assert res['detail'] == expected_answer['detail']

    @pytest.mark.parametrize(
        'query_data, expected_answer',
        test_created

    )
    @pytest.mark.asyncio
    async def test_bd_write(
        self, query_data, expected_answer, make_request, collection, get_access
    ):

        url = url_constructor('user_content/create')

        access_token = get_access()
        user_params = query_data['input_data']
        user_params['access_token'] = access_token

        reg_response = await make_request('post', url, params=user_params)

        status = reg_response.status
        assert status == expected_answer['status']

        if status == HTTPStatus.CREATED:
            cursor = collection.find({"relation_uuid": query_data['input_data']["relation_uuid"]})
            res = await cursor.to_list(length=1)

            assert res[0]["content"] == expected_answer['content']

    @pytest.mark.parametrize(
        'query_data, expected_answer',
        test_metrics
    )
    @pytest.mark.asyncio
    async def test_metrics(
        self, query_data, expected_answer, make_request, collection, get_access
    ):

        create_url = url_constructor('user_content/create')
        access_token = get_access()
        for n, user_params in enumerate(query_data['input_data']):
            user_params['access_token'] = access_token
            reg_response = await make_request('post', create_url, params=user_params)

            create_status = reg_response.status

            assert create_status == expected_answer['status']

        if create_status == HTTPStatus.CREATED:
            count_url = url_constructor('user_content/count')
            avg_url = url_constructor('user_content/avg_rating')

            count_params_like = {
                'relation_uuid': query_data['relation_uuid'],
                "object_type": 'like'

            }
            count_params_comment = {
                'relation_uuid': query_data['relation_uuid'],
                'object_type': 'comment'

            }
            count_params_rating = {
                'movie_uuid': query_data['relation_uuid'],
            }

            reg_response_like = await make_request(
                'get',
                count_url,
                args=count_params_like,
                params={}
            )

            res_like = await reg_response_like.json()

            assert res_like['count'] == expected_answer['likes']

            reg_response_comment = await make_request(
                'get',
                count_url,
                args=count_params_comment,
                params={}
            )
            res_comment = await reg_response_comment.json()

            assert res_comment['count'] == expected_answer['comments']

            reg_response_rating = await make_request(
                'get',
                avg_url,
                args=count_params_rating,
                params={}
            )
            res_rating = await reg_response_rating.json()
            if expected_answer['avg_rating'] == 0:
                assert res_rating['detail'] == "can't find this content"
            else:
                assert res_rating['result'] == expected_answer['comments']

    @pytest.mark.asyncio
    async def test_by_id(
        self, make_request, get_access
    ):
        create_url = url_constructor('user_content/create')

        access_token = get_access()

        user_params = {
            "relation_uuid": "d14b3ea9-b4db-4d73-a7d8-72815ac3eb67",
            "access_token": access_token,
            "object_type": "comment",
            "content": "final_test"
        }

        reg_response = await make_request('post', create_url, params=user_params)

        status = reg_response.status
        assert status == HTTPStatus.CREATED

        if status == HTTPStatus.CREATED:
            data = await reg_response.json()
            print(data)

            get_url = url_constructor('user_content/objects')

            get_args = {
                'object_id': data['_id'],
                'object_type': user_params['object_type']
            }

            reg_response = await make_request('get', get_url, args=get_args, params={})

            res = await reg_response.json()

            assert res['content']['content'] == user_params['content']
