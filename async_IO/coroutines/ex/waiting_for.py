'''
Timeouts
    - 適用的情境，當如果執行時間超過多少 wait_for 時間，就直接中止。


wait() 已經被 version 3.11 棄用?
! Unlike wait_for(), wait() does not cancel the futures when a timeout occurs.
! Deprecated since version 3.8, will be removed in version 3.11: Passing coroutine objects to wait() directly is deprecated.

Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html
'''
import asyncio

async def eternity():
    # Sleep for 10 seconds.
    await asyncio.sleep(10)
    print('yay!')
    
async def wait_but_not_cancel():
    # Sleep for 10 seconds.
    await asyncio.sleep(10)
    print('wait_but_not_cancel')
    
    
async def main():
    try:
        # 等待5秒後，如沒有完成則進入 except 返回 timeout。
        await asyncio.wait_for(eternity(), timeout=5)
    except asyncio.TimeoutError:
        print('timeout !!!')


async def main2():
    # 持續等待直到完成任務
    task = asyncio.create_task(wait_but_not_cancel())
    await asyncio.wait({task})
    

asyncio.run(main()) # timeout !!!
# asyncio.run(main2()) # timeout !!!

