'''

Reference:
    - https://juejin.cn/post/7095400034165850148
'''
import asyncio
import time

# 非同步函式
async def say_after(delay, what):
    """say_after function."""
    await asyncio.sleep(delay)
    print(what)

async def main():
    '''main predure.'''
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")


# 同步函式
def funOne():
    return ("function one.")

def funTwo():
    return ("function two.")

def funThree():
    return ("function three.")

def run():
    print(funOne())
    print(funTwo())
    print(funThree())
    
if __name__ == '__main__':
    # 非同步函式執行
    asyncio.run(main())
    
    # 同步函式執行
    run()
    
