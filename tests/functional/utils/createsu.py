from http import HTTPStatus

import aiohttp
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound


from tests.functional.db.models.users import Users, Roles
from tests.functional.utils.url_constuctor import url_constructor
from tests.functional.settings import settings
from tests.functional.db.models.users import Users, Roles


async def admin_mode(session):

    req_url = url_constructor('authorization/register')
    params = {
        "login": settings.admin_login,
        "password": settings.admin_password
    }
    client = aiohttp.ClientSession()
    response = await client.post(req_url, json=params)

    print(response)

    if response.status == HTTPStatus.ACCEPTED:

        query_role = select(Roles).where(Roles.level == 5)
        query_role_result = await session.execute(query_role)
        try:
            role = query_role_result.one()
        except NoResultFound:
            role = None

        if not role:
            role = Roles(
                name='admin',
                desc='admin',
                level=settings.admin_level
            )

            session.add(role)

        query_user = select(Users).where(
            Users.login == params['login']
        )
        query_user_result = await session.execute(query_user)
        user = query_user_result.scalar_one()

        user.role = role.uuid

        session.add(user)
