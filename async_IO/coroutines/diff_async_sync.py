"""
Reference:
    - https://www.maxlist.xyz/2020/03/29/python-coroutine/

Note:
    - make sure what's different between async and sync.
    - please check the process of async.
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


def do_sync_something(num: int):
    """
    do something with sync.
    :param num:
    :return:
    """
    print(f'task {num}: the first step.')
    time.sleep(2)
    print(f'task {num}: the second step.')


if __name__ == '__main__':
    start = time.time()

    # Note: please note the different between async and sync.

    # async
    loop = asyncio.get_event_loop()
    task = []
    task = [do_something(i) for i in range(5)]
    loop.run_until_complete(asyncio.wait(task))
    end2 = time.time()

    # sync
    res = [do_sync_something(i) for i in range(5)]
    end = time.time()

    print('end2', end2 - start)
    print('end', end - start)