'''
Demo: 使用 lock 來處理錯誤狀況，需要撰寫程式並共享相同變數，會產生race condition。
    - 共享相同變數 database_value
    - 使用 with 讓寫法更簡潔一點。

Reference:
    - https://www.youtube.com/watch?v=usyg5vbni34
'''
from threading import Thread, Lock
import time


# 通常會共享變數的狀況，有可能會是收集最終資訊的 dashboard 和 多個 Object 對某個 Object 進行運作。
database_value = 0


def increase(lock):
    global database_value

    # 使用 with 讓寫法更簡潔一點。
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy



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
    




