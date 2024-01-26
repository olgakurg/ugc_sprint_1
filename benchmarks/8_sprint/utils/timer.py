import time


def timer(iteration: int):
    def wrap(func):
        def dec(*args, **kwargs):
            result = []
            for iter in range(iteration):
                start = time.perf_counter()
                func(*args, **kwargs)
                stop = time.perf_counter()
                res = stop - start
                result.append(res)
            avg_result = sum(result) / len(result)

            return avg_result

        return dec

    return wrap


@timer(10)
def test(rn):
    for i in range(rn):
        a = i * i


if __name__ == "__main__":
    a = test(1000000)

    print(a)
