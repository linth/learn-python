"""
References
- https://docs.python.org/3.6/library/asyncio-task.html
"""
import asyncio


async def compute(x, y):
    print(f"compute {x} + {y} .........")
    await asyncio.sleep(3)
    return x+y


async def sum(x, y):
    res = await compute(x, y)
    print(f"{x} + {y} = {res}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sum(1, 2))
    loop.close()

    # TODO:
    #  1) Future with run_until_complete()
    #  2) Future with run_forever()
    #  3) Task
    #  4) Parallel execution of tasks
