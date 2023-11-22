import time
import functools


@functools.lru_cache()
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def func1():
    print(fib(100))
    print("func1 завершен")


def func2():
    print(fib(100))
    print("func2 завершен")


def main():
    start = time.time()
    func1()
    func2()
    finish = time.time()
    print(finish - start)




main()