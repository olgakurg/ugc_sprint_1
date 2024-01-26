from uuid import uuid4

import pytest
import pytest_asyncio

import motor.motor_asyncio

from utils.tokengenerator import token_generate

from utils.url_constuctor import url_constructor
from settings import settings


@pytest.fixture
def client():
    return motor.motor_asyncio.AsyncIOMotorClient(
        settings.uc_host, settings.uc_port
    )


@pytest.fixture
def db(client):
    return client[settings.uc_database]


@pytest.fixture
def collection(db):
    collection = db[settings.uc_collections]
    collection.drop()
    return collection


# @pytest_asyncio.fixture(scope='function')
# def fake_engine():
#     engine = create_engine(settings.dsl_auth_sync)
#     Base.metadata.create_all(engine)
#     yield create_async_engine(settings.dsl_auth)
#     Base.metadata.drop_all(engine)


# @pytest_asyncio.fixture(scope='function')
# async def fake_session(fake_engine):

#     async_sesion_factory = sessionmaker(
#         fake_engine,
#         expire_on_commit=False,
#         class_=AsyncSession
#     )
#     async with async_sesion_factory() as session:
#         yield session


@pytest_asyncio.fixture()
def get_access():
    def inner():
        return token_generate('admin', uuid4(), uuid4())
    return inner
