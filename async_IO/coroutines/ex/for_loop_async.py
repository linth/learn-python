'''
同時併發 (concurrency) 執行 for-loop 搭配使用 async 來執行
    - asyncio.gather() 併發運行任務

情境是有三個任務，分別為執行 10, 2, 4 次的 for-loop，三個任務會併發式執行處理完畢後，由return 的 task 接收。

Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html

'''
import asyncio
import time


async def sum(task_name, max_nums):
    start_time = time.time()
    
    for i in range(max_nums):
        print(f'task {task_name}: i={i}')
        await asyncio.sleep(1)
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f'task {task_name} spend time: {total_time}')
    
    return total_time


async def main():
    start_time = time.time()
    
    task = await asyncio.gather(
        sum('1', 10),
        sum('2', 2),
        sum('3', 4),
    )
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # 會將 task 內的任務執行完畢後的結果，存到 task list 裡面。
    print(task)
    
    # 原本三個任務，總共會需要 10 + 2 + 4 = 16秒，但使用 concurrency則加快速度僅需要 10秒多
    print('total_time', total_time)
    
asyncio.run(main())