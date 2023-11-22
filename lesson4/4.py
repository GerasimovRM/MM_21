def cache(func):
    dict_vars = {}

    def new_func(*args):
        if args in dict_vars:
            return dict_vars[args]
        result = func(*args)
        dict_vars[args] = result
        return result

    return new_func


@cache
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(100))