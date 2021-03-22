"""
References:
    - https://realpython.com/async-io-python/

:keyword
    - Coroutines (specialized generator functions) are the heart of async IO in Python
    - async/await: two new Python keywords that are used to define coroutines

    - Concurrency: threading, async IO
    - Parallelism: Multiprocessing
"""
import asyncio
import time


async def count():
    print('One')
    await asyncio.sleep(2)
    print('Two')


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    s = time.perf_counter()
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    elapsed = time.perf_counter() - s

    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
