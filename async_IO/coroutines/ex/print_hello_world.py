'''
列印出 hello 後，隔一秒再列印出 world.
    - 非同步阻塞 (synchronous + blocking)
    
    
Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html
'''
import asyncio
import time


async def main():
    print('hello')
    await asyncio.sleep(1)    
    print('world')
    

asyncio.run(main())