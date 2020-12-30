import asyncio


async def show_hello():
    await asyncio.sleep(3)
    print('hello')
    return 'hello'


async def show_hi(msg: str):
    if msg == 'hello':
        print('hi, I got it.')

    # NOTE: you can add async functions to do something.
    await show_hello()

    # NOTE: you can add sync functions to do something.
    show_end()


def show_end():
    print('ending the processing.')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    task = [
        asyncio.ensure_future(show_hello()),
        asyncio.ensure_future(show_hi('hello')),
    ]

    loop.run_until_complete(asyncio.wait(task))
