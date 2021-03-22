import asyncio
import time


def show_hello():
    print('hello ')

async def show_world():
    print('world.')

async def say_after(delay: int, what: str):
    await asyncio.sleep(delay)
    print(what)

async def show_helloworld():
    await show_world()
    # await asyncio.sleep(1)
    show_hello()
    
async def main():
    show_hello()
    await asyncio.sleep(1)
    show_world()

async def main2():
    print('time: ', time.strftime('%X'))
    await say_after(1, 'Hello ')
    print('time: ', time.strftime('%X'))
    await say_after(2, 'world.')
    print('time: ', time.strftime('%X'))

async def main3():
    print(f"time: {time.strftime('%X')}")
    task1 = asyncio.create_task(say_after(1, 'Hello '))
    task2 = asyncio.create_task(say_after(2, 'World.'))
    # print(f"time: {time.strftime('%X')}")
    await task1
    await task2
    print(f"time: {time.strftime('%X')}")

async def main4():
    # await function_that_returns_a_future_object()
    await show_world()
    show_hello()

    # this is also valid:
    await asyncio.gather(
        # function_that_returns_a_future_object(),
        show_world()
        # some_python_coroutine()
    )

if __name__ == '__main__':
    # asyncio.run(main())
    # asyncio.run(show_helloworld())
    # asyncio.run(main2())
    # asyncio.run(main3())
    asyncio.run(main4())

