import time
import asyncio


async def func1(x):
    print(x ** 2)
    await asyncio.sleep(3)
    print("func1 завершен")


async def func2(x):
    print(x ** 0.5)
    await asyncio.sleep(3)
    print("func2 завершен")


async def main():
    start = time.time()
    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func2(-4))
    await task1
    await task2
    finish = time.time()
    print(finish - start)


asyncio.run(main())
