'''
concurrent.futures — 創立非同步任務
    - 請跟thread_pool_executor 範例一起參考

ProcessPoolExecutor.map()改變 chunksize 來加速
    - 使用 Proc essPoolExecutor.map()的時候，可以透過改變 chunksize 來加速，預設的 chunksize 是 1。
    - 所以如果遇到一些高 CPU-bound 但低執行時間的任務時，可以改變 chunksize 來進行加速。
    - 舉例同樣採用費氏數列，但是這次要計算很多很多的小數字：

TODO: 思考為什麼不使用 multiprocessing ??

Reference:
    - https://blog.louie.lu/2017/08/01/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-06-concurrent-futures/
    - https://docs.python.org/3/library/concurrent.futures.html
'''
import concurrent.futures
import time

 
FIBS = [5, 5, 5, 5, 5, 10, 10, 10, 10] * 50

def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def process(chunksize=1):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, fib_value in zip(FIBS, executor.map(fib, FIBS, chunksize=chunksize)):
            s = "%d's fib number is %d" % (number, fib_value)
 
def main():
    for num in FIBS:
        s = "%d's fib number is %d" % (num, fib(num))
        
if __name__ == '__main__':
    
    s = time.time()
    process()
    e = time.time()
    print('total time:', e-s)
    
    
    s = time.time()
    process(32)
    e = time.time()
    print('total time:', e-s)
    