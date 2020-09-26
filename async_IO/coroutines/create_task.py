"""
Reference
    - https://www.maxlist.xyz/2020/03/29/python-coroutine/
"""
import asyncio
import time
from color.IeColor import IeColor


async def do_something(num: int):
    """
    do something with async.
    :param num:
    :return:
    """
    print(IeColor().pink, f'task {num}: the first step.', IeColor().end)
    await asyncio.sleep(2)
    print(IeColor().warning, f'task {num}: the second step.', IeColor().end)


if __name__ == '__main__':

    # method 1: input/output are async.
    start = time.time()
    loop = asyncio.get_event_loop()
    task = [do_something(i) for i in range(5)]
    loop.run_until_complete(asyncio.wait(task))
    end = time.time()

    # method 2: order-based event.
    start2 = time.time()
    loop2 = asyncio.get_event_loop()
    task2 = [
        asyncio.ensure_future(do_something(1)),
        asyncio.ensure_future(do_something(2)),
        asyncio.ensure_future(do_something(3)),
    ]
    loop2.run_until_complete(asyncio.wait(task2))
    end2 = time.time()

    # method 3:
    start3 = time.time()
    loop3 = asyncio.get_event_loop()
    task3 = [do_something(i) for i in range(5)]
    task3.append(asyncio.ensure_future(do_something(5)))
    task3.append(asyncio.ensure_future(do_something(6)))
    task3.append(asyncio.ensure_future(do_something(7)))
    loop3.run_until_complete(asyncio.wait(task3))

    print(end - start) # 2.0020759105682373
    print(end2 - start2) # 2.000319480895996
    print(time.time() - start3) # 2.0008456707000732
