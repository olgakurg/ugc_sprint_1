"""Setup for pytest_aiohttpreq plugin."""

from setuptools import setup

setup(
    name='pytest-aiohttpreq_p',
    version='0.1.0',
    description='fictures fo aiohttp for async requests',
    url='',
    author='ortariot',
    author_email='ortariot@gmail.com',
    license='ortariot',
    py_modules=['pytest_aiohttpreq_p'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['iohttpreq_p = pytest_aiohttpreq_p', ], },
)
