import matplotlib.pyplot as plt
from tqdm import tqdm

from db.clickhousestore import ClickHouse
from db.vertica import Vertica
from settings.settings import settings
from utils.data_generator import data_generator
from utils.timer import timer


@timer(10)
def inser_to_db(db, data: list):
    column = ['id', 'user_id', 'value', 'event_time', 'event_type']
    db.write(data, settings.event_table, column)


@timer(10)
def get_from_db(db, limit: int):
    db.read(settings.event_table, limit)


def write_benchmark(func, test_db: list) -> dict[str, list]:
    results = {'batch_value': []}
    for batch_value in tqdm(range(1, 2000, 1000)):
        data = data_generator(batch_value)
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
    for limit in tqdm(range(1, 2000, 1000)):

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

    write_res = write_benchmark(inser_to_db, [ch_store, vertica_store])
    plot(write_res)

    read_res = read_benchmark(get_from_db, [ch_store, vertica_store])
    plot(read_res)
