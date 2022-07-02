'''
Demo: 錯誤狀況，需要撰寫程式並共享相同變數，會產生race condition。
    - 學習找到錯誤跟原因!!

Reference:
    - https://www.youtube.com/watch?v=usyg5vbni34
'''
from threading import Thread
import time

database_value = 0


def increase():
    global database_value

    local_copy = database_value

    # processing
    local_copy += 1
    time.sleep(0.1)

    database_value = local_copy


if __name__ == '__main__':
    threads = []
    num_threads = 10
    
    print('start value', database_value)
    
    # create threads.
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print('end value', database_value)
        
    print('finished !!')
    
    # 會有錯誤資訊，database_value 應該為2
    '''
    start value 0
    end value 1
    finished !!
    '''



