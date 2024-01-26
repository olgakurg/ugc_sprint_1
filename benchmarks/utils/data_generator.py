import random
import string
from time import time
from uuid import uuid4

events = (
    'click', 'play', 'read', 'start',
    'search', 'push', 'run', 'login', 'logout'
)


def generate_random_string():
    length = random.randint(1, 100)
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def data_generator(batch_size: int) -> list:
    data = [
        (
            str(uuid4()),
            str(uuid4()),
            str(uuid4()),
            random.choice(events),
            int(time()),
            generate_random_string(),


        ) for i in range(batch_size)
    ]

    return data


if __name__ == "__main__":

    data = data_generator(1)

    print(data)
