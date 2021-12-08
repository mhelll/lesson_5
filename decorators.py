def decorator(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper


def fabric_decorators(arg_decorator):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    return decorator


@decorator
def test_1(arg1):... #test_1 = decoratoR(test_1)


@fabric_decorators(123)
    def test_2(arg1):...



if __name__ == '__main__':
    test_1(5)