'''
使用 asyncio.task()
    - 當遇到大量非同步工作時，可利用 asyncio 的 task 將非同步工作包裝起來，一起透過 gather 執行，並取回執行結果。


[問題] 使用 task 方式，跟直接使用 gather 有什麼區別?

Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html
    - https://officeguide.cc/python-asyncio-aiohttp-asynchronous-io-tutorial-examples/
'''
import asyncio
import time


async def sum(task_name, max_nums):
    s = time.time()

    for i in range(max_nums):
        await asyncio.sleep(1)

    e = time.time()
    print(f'task name: {task_name}, spend time: {e-s}')
    
    return e-s


async def main():
    # 建立 task 列表
    tasks = []
    tasks.append(asyncio.create_task(sum('1', 10)))
    tasks.append(asyncio.create_task(sum('2', 4)))
    tasks.append(asyncio.create_task(sum('3', 7)))
    
    # 執行所有 tasks，注意要有 return 才可以收集 task 結果。
    results = await asyncio.gather(*tasks)
    print('results', results)


asyncio.run(main())
