"""
References
    - https://ithelp.ithome.com.tw/articles/10199408
    - https://docs.python.org/3/library/asyncio-task.html
"""
import asyncio


async def show_hello():
    print("Hello")
    await asyncio.sleep(5)
    print("world.")


async def show_hi():
    await asyncio.sleep(1)
    print("Hi")
    await asyncio.sleep(3)
    print("everyone")


if __name__ == '__main__':
    # TODO: get_event_loop for python 3.7 before.
    #  if using after python 3.7, you can use .run() function.
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(show_hello())

    # the process of task is show_hello() -> show_hi().
    task = [
        asyncio.ensure_future(show_hello()),
        asyncio.ensure_future(show_hi()),
    ]
    loop.run_until_complete(asyncio.wait(task))
