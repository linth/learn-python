'''
混合情境: Running in Threads (請跟 coroutine_in_threads.py 一起參考)
    - Asynchronously run function func in a separate thread.
    - 非同步函式會被在不同的 threads 下執行任務。
    - 如果在任何的 coroutine 中，直接呼叫 blocking_io()，都會造成阻塞事件循環，導致額外1秒時間執行。
    - 然而，此次範例改用asyncio.to_thread()，就可以在不同 thread 運行而不會阻塞事件循環。
    
此範例主要是在 非同步的 main function，執行同步任務 blocking_io。
    - to_thread(function, *arg, **kwargs)
    
Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html 
'''
import asyncio
import time


def blocking_io():
    start_time = time.time()
    print(f"start blocking_io at {start_time}")
    
    time.sleep(3)
    
    end_time = time.time()
    print(f"blocking_io complete at {end_time}")
    
    print("total time:", end_time - start_time)
    
def show_hello():
    # 增加同步任務
    print('hello')
    
async def show_world():
    # 增加非同步任務
    print('world')

async def main():
    start_time = time.time()
    print("start main at", start_time)
    
    # 如果在任何的 coroutine 中，直接呼叫 blocking_io()，都會造成阻塞事件循環，導致額外1秒時間執行。
    # 然而，此次範例改用asyncio.to_thread()，就可以在不同 thread 運行而不會阻塞事件循環。
    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.to_thread(show_hello),
        asyncio.to_thread(show_hello),
        # asyncio.sleep(1)
        asyncio.create_task(show_world())
    )
    
    end_time = time.time()
    print("finished main at", end_time)
    print("total time:", end_time - start_time)
    

asyncio.run(main())

'''
start main at 1654847279.8828802
world
start blocking_io at 1654847279.8858826
hello
hello
blocking_io complete at 1654847282.8901618
total time: 3.004279136657715
finished main at 1654847282.8901618
total time: 3.007281541824341
'''
