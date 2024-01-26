import asyncio

import matplotlib.pyplot as plt
from tqdm import tqdm

from db.clickhousestore import ClickHouse
from db.vertica import Vertica
from db.mongosrore import Mongo
from db.pgstore import Postgres
from settings.settings import settings
from utils.data_generator import data_generator
from utils.timer import timer


@timer(1)
def inser_to_db(db, data: list):

    column = ['id', 'relation_uuid', 'user_uuid', 'object_type', 'timestamp', 'content']
    db.write(settings.event_table, column, data)


@timer(1)
def get_from_db(db, limit: int):

    db.read(settings.event_table, limit)


@timer(1)
def single_inser_to_db(db, count):

    column = ['id', 'relation_uuid', 'user_uuid', 'object_type', 'timestamp', 'content']
    for iter in range(count):
        data = data_generator(1)
        db.write(settings.event_table, column, data)


def write_benchmark(func, test_db: list) -> dict[str, list]:

    results = {'batch_value': []}
    for batch_value in tqdm(range(1, 50000, 1000)):

        results['batch_value'].append(batch_value)

        for db in test_db:
            res_time = func(db, data)

            if db.__class__.__name__ in results:
                results[db.__class__.__name__].append(res_time)
            else:
                results[db.__class__.__name__] = [res_time]

    return results


def read_benchmark(func, test_db: list) -> dict[str, list]:

    results = {'limit': []}
    for limit in tqdm(range(1, 50000, 5000)):

        results['limit'].append(limit)

        for db in test_db:
            res_time = func(db, limit)

            if db.__class__.__name__ in results:
                results[db.__class__.__name__].append(res_time)
            else:
                results[db.__class__.__name__] = [res_time]

    return results


def single_write(func, test_db: list) -> dict[str, list]:
    results = {'limit': []}
    for limit in tqdm(range(1, 1000, 100)):
        results['limit'].append(limit)
        for db in test_db:
            res_time = func(db, limit)

            if db.__class__.__name__ in results:
                results[db.__class__.__name__].append(res_time)
            else:
                results[db.__class__.__name__] = [res_time]
    return results


def plot(graph_date):
    axis = list(graph_date.keys())

    print(axis)
    for c_axis in axis[1:]:
        plt.plot(graph_date[axis[0]], graph_date[c_axis])

    plt.legend(axis[1:])
    plt.xlabel('data value')
    plt.ylabel('Time,[s]')

    plt.grid()
    plt.show()


if __name__ == '__main__':
    ch_store = ClickHouse(settings.clickhuse_address, settings.clickhuse_port)

    vertica_store = Vertica(
        settings.vertica_address,
        settings.vertica_port,
        settings.vertica_user,
        '',
        settings.vertica_db_name
    )

    mongostore = Mongo(
        settings.mongo_host,
        settings.mongo_port,
        settings.mongo_db_name
    )

    pgstore = Postgres(
        settings.pg_host,
        settings.pg_port,
        settings.pg_db_name,
        settings.pg_user,
        settings.pg_password
    )

    write_res = write_benchmark(
        inser_to_db, [ch_store, mongostore])
    plot(write_res)

    read_res = read_benchmark(
        get_from_db, [ch_store, pgstore])
    plot(read_res)

    single_write_res = single_write(single_inser_to_db, [ch_store, mongostore, pgstore])
    plot(single_write_res)
