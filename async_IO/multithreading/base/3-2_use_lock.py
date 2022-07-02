'''
Demo: 使用 lock 來處理錯誤狀況，需要撰寫程式並共享相同變數，會產生race condition。
    - 學習使用 lock 方式

Reference:
    - https://www.youtube.com/watch?v=usyg5vbni34
'''
from threading import Thread, Lock
import time

database_value = 0


def increase(lock):
    global database_value
    
    lock.acquire() # 獲得 lock，並從此開始會使用 lock 進行變數鎖定。
    local_copy = database_value
    
    # processing
    local_copy += 1
    time.sleep(0.1)
    
    database_value = local_copy
    lock.release() # 釋放 lock



if __name__ == '__main__':
    lock = Lock()
    print('start value', database_value)
    
    # create threads.
    thread1 = Thread(target=increase, args=(lock, ))
    thread2 = Thread(target=increase, args=(lock, ))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print('end value', database_value)
    print('finished !!')


