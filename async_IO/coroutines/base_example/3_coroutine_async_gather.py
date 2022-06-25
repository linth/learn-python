'''
使用 asyncio.gather() 來執行非同步任務
    - asyncio.gather() 併發運行任務，同時併發 (concurrency) 執行。
    - 原本三個任務，總共會需要 10 + 2 + 4 = 16秒，但使用 concurrency則加快速度僅需要 10秒多
'''
import asyncio
import time


async def sum(task_name, max_nums):
    s = time.time()
    
    for i in range(max_nums):
        # print(f'task {task_name}: i={i}')
        await asyncio.sleep(1)
        
    e = time.time()
    print(f'task name: {task_name}, spend time: {e-s}')


async def main():
    start_time = time.time()
    
    await asyncio.gather(
        sum('1', 10),
        sum('2', 2),
        sum('3', 4),
    )

    end_time = time.time()
    total_time = end_time - start_time

    # 原本三個任務，總共會需要 10 + 2 + 4 = 16秒，但使用 concurrency則加快速度僅需要 10秒多
    print('total_time', total_time)

asyncio.run(main())

