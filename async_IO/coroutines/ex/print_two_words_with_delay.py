'''
隔幾秒後，列印出 hello 後，隔幾秒再列印出 world.
    - 非同步阻塞 (synchronous + blocking)
    
    
Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html

'''
import asyncio
import time


async def print_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
    
async def main():
    # 按照順序執行
    
    print(f"started at {time.strftime('%X')}")
    
    await print_after(1, 'hello')
    await print_after(2, 'world')
    
    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(main())