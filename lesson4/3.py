import time


def logging(func):
    count = 0

    def new_func(*args, **kwargs):
        nonlocal count
        print("-" * 20)
        print(f'Args: {args}')
        print(f'Named args: {kwargs}')
        print(f'Функцию до этого вызывали {count} раз')
        count += 1
        result = func(*args, **kwargs)
        print("-" * 20)
        return result
    return new_func


def timer(func):
    def new_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finished_time = time.time()
        print(f'Time work: {finished_time - start_time}')
        return result
    return new_func


@logging
@timer
def f(x):
    return x ** 2
# f = logging(f)


def g(x):
    return x ** 2


print(f(10))
print(f(10))
print(f(10))
print(f(10))
