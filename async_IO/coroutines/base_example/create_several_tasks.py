'''
使用 create_task() 來建立多個小任務

Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html
'''
import asyncio
import time


async def print_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    # 任務1
    task1 = asyncio.create_task(
        print_after(1, 'hello')
    )
    # 任務2
    task2 = asyncio.create_task(
        print_after(2, 'world')
    )
    
    
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")
    
    
# 注意，预期的输出顯示程式碼的運行時間比之前快了 1 秒: (可能使用此方式會加快速度!!!)
asyncio.run(main())