"""
References
-
"""
import asyncio


async def task1():
    """
    async task1.
    :return:
    """
    print(f"this is task1.")


async def task2():
    """
    async task2.
    :return:
    """
    print(f"this is task2.")
    await task3()


async def task3():
    """
    async task3.
    :return:
    """
    print(f"this is task3.")


def task4():
    """
    task 4.
    :return:
    """
    print(f"this is task4.")


if __name__ == '__main__':
    # TODO: to simulate the situation of AJAX + process following order.
    loop = asyncio.get_event_loop()

    task = [
        asyncio.ensure_future(task1()),
        asyncio.ensure_future(task2()),
        asyncio.ensure_future(task3()),
    ]

    loop.run_until_complete(asyncio.wait(task))
