'''
比較使用 task & 不使用 task 方式哪個執行效率高?
    - 目前測試看不太出來差異，可是的問題是範例使用sleep方式?

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
    s = time.time()
    
    # 建立 task 列表
    tasks = []
    tasks.append(asyncio.create_task(sum('1', 10)))
    tasks.append(asyncio.create_task(sum('2', 4)))
    tasks.append(asyncio.create_task(sum('3', 7)))
    
    # 執行所有 tasks，注意要有 return 才可以收集 task 結果。
    results = await asyncio.gather(*tasks)
    print('results', results)
    
    e = time.time()
    print(f'Main() total time: {e-s}')
    

async def main2():
    s = time.time()
    
    await asyncio.gather(
        sum('1', 10),
        sum('2', 4),
        sum('3', 7),
    )
    
    e = time.time()
    print(f'Main2() total time: {e-s}')


if __name__ == '__main__':
    asyncio.run(main())
    
    asyncio.run(main2())
    
    
# task name: 2, spend time: 4.035509347915649
# task name: 3, spend time: 7.052590847015381
# task name: 1, spend time: 10.08663296699524
# results [10.08663296699524, 4.035509347915649, 7.052590847015381]
# Main() total time: 10.088642835617065
# task name: 2, spend time: 4.03019905090332
# task name: 3, spend time: 7.046497821807861
# task name: 1, spend time: 10.068386793136597
# Main2() total time: 10.068386793136597