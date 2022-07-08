'''
task 1 -> task 2 -> task 3 -> ...

'''
import asyncio


async def task1():
    print('execute task 1.')
    
    print('task 1 call task 2.')
    await task2()
    print('end of task 2 by task 1.')
    # await asyncio.sleep(5)
    print('end of task 1.')



async def task2():
    print('execute task 2.')
    
    print('task 2 call task 3.')
    await task3()
    print('end of task 3 by task 2.')
    
    # await asyncio.sleep(3)
    print('end of task 2.')
    
    

async def task3():
    print('execute task 3.')
    await asyncio.sleep(2)
    print('end of task 3.')
    
    

async def main():
    print('execute main.')
    await task1()
    # await task2()
    # await task3()
    print('end of main.')


if __name__ == '__main__':
    asyncio.run(main())
    
