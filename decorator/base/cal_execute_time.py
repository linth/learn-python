'''
思考可以使用裝飾器來提供函式的執行所需時間？
    - 單純裝飾器
    - 使用裝飾器工廠
    
TODO: 可以參考 timeit library 來測試學習
'''
import time

def spend_how_much_time(callback):
    def run():
        start_time = time.time()
        callback()
        end_time = time.time()
        print(f'total time: ', end_time - start_time)
    return run

@spend_how_much_time
def function1():
    sum = 0
    for i in range(1000000001):
        sum += i
    print(f'sum: ', sum)


function1()

# todo: using decorator factory.