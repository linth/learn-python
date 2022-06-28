'''
decorator + return value

Reference:
    - https://www.youtube.com/watch?v=QqRvteWBSWg&t=74s
'''
import time

def cal_executed_time(func):
    def wrapper(num):        
        start = time.time()
        result = func(num)
        end = time.time()        
        print(end - start)
        return result    
    return wrapper


@cal_executed_time
def cal_sum(num):
    sum = 0
    for i in range(num):
        sum += i
    return sum

        
if __name__ == '__main__':
    res = cal_sum(100000000)
    print('res', res)
    