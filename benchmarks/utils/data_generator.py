import string
import random
from datetime import datetime, timedelta

from uuid import uuid4

events = (
    'click', 'play', 'read', 'start',
    'search', 'push', 'run', 'login', 'logout'
)


def data_generator(batch_size: int) -> list:
    data = [
        (
            uuid4(),
            str(uuid4()),
            random.randint(0, 1000),
            datetime(2024, 1, 1, hour=0, minute=0, second=0),
            random.choice(events),


        ) for i in range(batch_size)
    ]

    return data


if __name__ == "__main__":

    data = data_generator(1)

    print(data)
