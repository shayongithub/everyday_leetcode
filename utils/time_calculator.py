import time


def time_execution(func, **kwargs):
    start = time.time()
    func(**kwargs)
    end = time.time()
    return end - start
