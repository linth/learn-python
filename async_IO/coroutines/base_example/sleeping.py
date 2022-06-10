'''
Sleeping for asyncio.
    - 範例是每秒會顯示最近的 date, 直到超過5秒
    
[注意!]
! Changed in version 3.10: Removed the **loop** parameter.

Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html
'''
import asyncio
import datetime


async def display_date():
    loop = asyncio.get_running_loop()    
    end_time = loop.time() + 5

    while True:
        print(datetime.datetime.now())
        
        if (loop.time() + 1) >= end_time:
            break
        await asyncio.sleep(1)
        
asyncio.run(display_date())

'''
2022-06-10 11:13:10.983498
2022-06-10 11:13:11.996169
2022-06-10 11:13:13.011120
2022-06-10 11:13:14.026497
2022-06-10 11:13:15.038622
'''