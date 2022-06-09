'''
階乘 factorial 搭配使用 async 來執行

Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html

'''
import asyncio
import time


async def factorial(name, number):
    start_time = time.time()
    f = 1
        
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
        
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Task {name}: factorial({number}) = {f}, total time: {total_time}")
    
    return f


async def main():
    
    # 同時並發處理
    L = await asyncio.gather(
        factorial('A', 2),
        factorial('B', 3),
        factorial('C', 2),
        factorial('D', 20),
    )
    
    print(L)
    
asyncio.run(main())

'''
請注意A,B,C,D 任務執行的狀況

Task A: Compute factorial(2), currently i=2...
Task B: Compute factorial(3), currently i=2...
Task C: Compute factorial(2), currently i=2...
Task D: Compute factorial(20), currently i=2...
Task A: factorial(2) = 2, total time: 1.012312889099121
Task C: factorial(2) = 2, total time: 1.012312889099121
Task B: Compute factorial(3), currently i=3...
Task D: Compute factorial(20), currently i=3...
Task B: factorial(3) = 6, total time: 2.019624948501587
Task D: Compute factorial(20), currently i=4...
Task D: Compute factorial(20), currently i=5...
Task D: Compute factorial(20), currently i=6...
Task D: Compute factorial(20), currently i=7...
Task D: Compute factorial(20), currently i=8...
Task D: Compute factorial(20), currently i=9...
Task D: Compute factorial(20), currently i=10...
Task D: Compute factorial(20), currently i=11...
Task D: Compute factorial(20), currently i=12...
Task D: Compute factorial(20), currently i=13...
Task D: Compute factorial(20), currently i=14...
Task D: Compute factorial(20), currently i=15...
Task D: Compute factorial(20), currently i=16...
Task D: Compute factorial(20), currently i=17...
Task D: Compute factorial(20), currently i=18...
Task D: Compute factorial(20), currently i=19...
Task D: Compute factorial(20), currently i=20...
Task D: factorial(20) = 2432902008176640000, total time: 19.183733224868774
[2, 6, 2, 2432902008176640000]
'''