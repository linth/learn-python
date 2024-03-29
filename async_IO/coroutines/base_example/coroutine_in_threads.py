'''
Running in Threads
    - Asynchronously run function func in a separate thread.
    - 非同步函式會被在不同的 threads 下執行任務。
    - 如果在任何的 coroutine 中，直接呼叫 blocking_io()，都會造成阻塞事件循環，導致額外1秒時間執行。
    - 然而，此次範例改用asyncio.to_thread()，就可以在不同 thread 運行而不會阻塞事件循環。
    
此範例主要是在 非同步的 main function，執行同步任務 blocking_io。
    - to_thread(function, *arg, **kwargs)
TODO: 應該要確認 main(), blocking_io() 的 thread id.
    
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
    

async def main():
    start_time = time.time()
    print("start main at", start_time)
    
    # 如果在任何的 coroutine 中，直接呼叫 blocking_io()，都會造成阻塞事件循環，導致額外1秒時間執行。
    # 然而，此次範例改用asyncio.to_thread()，就可以在不同 thread 運行而不會阻塞事件循環。
    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1)
    )
    
    end_time = time.time()
    print("finished main at", end_time)
    print("total time:", end_time - start_time)
    

asyncio.run(main())