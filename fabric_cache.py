import time
from collections import OrderedDict
from functools import lru_cache

def cache(maxsize=3):
    def decorator(fn):
        dict_cahce = OrderedDict()

        def wrapper(*args):
            if args not in dict_cahce:
                if len(dict_cahce) == maxsize:
                    dict_cahce.popitem(last=False)
                result = fn(*args)
                dict_cahce[args] = result

            return dict_cahce[args]
        return wrapper

@cache(3)
def my_sleep():
    time.sleep(3)

@lru_cache(maxsize=None)
def my_sleep():
    time.sleep1(3)


if __name__ == '__main__':
    t0 = time.time()

    print(my_sleep())
    print(my_sleep())

    print(time.time() - t0)