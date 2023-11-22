import asyncio
import time
import functools


async def fib(n):
    if n <= 2:
        return 1
    else:
        a = asyncio.create_task(fib(n - 1))
        b = asyncio.create_task(fib(n - 2))
        a = await a
        b = await b
        return a + b


async def func1():
    x = await fib(20)
    print(x)
    print("func1 завершен")


async def func2():
    x = await fib(20)
    print(x)
    print("func2 завершен")


async def main():
    start = time.time()
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    await task1
    await task2
    finish = time.time()
    print(finish - start)


asyncio.run(main())
