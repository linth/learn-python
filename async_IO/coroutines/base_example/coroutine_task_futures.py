'''
可等待 object 有三種主要類型: 
    - 協程 (coroutine), 
    - 任務 (task)
    - Future

Future:
    - Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。
    - 當一個 Future object 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。


Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html
'''
import asyncio


async def nested():
    return 42

async def show_hello():
    print('hello')
    return 'hello'

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # nested()
    
    # 1. 協程實作
    # Let's do it differently now and await it:
    print(await nested())  # will print "42".
    
    # 2. 任務實作
    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    #! create_task 只適合單一任務，如多任務則需使用 gather
    task = asyncio.create_task(nested())
    await task
    print(task)
    
    # Futures實作
    # TODO: 需補充範例 examples.
    await asyncio.gather(show_hello(),
                         nested())

asyncio.run(main())