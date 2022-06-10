'''
Timeouts
    - 適用的情境，當如果執行時間超過多少 wait_for 時間，就直接中止。


Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html
'''
import asyncio

async def eternity():
    # Sleep for 10 seconds.
    await asyncio.sleep(10)
    print('yay!')
    

async def main():
    try:
        # 等待5秒後，如沒有完成則進入 except 返回 timeout。
        await asyncio.wait_for(eternity(), timeout=5)
    except asyncio.TimeoutError:
        print('timeout !!!')
        

asyncio.run(main()) # timeout !!!
