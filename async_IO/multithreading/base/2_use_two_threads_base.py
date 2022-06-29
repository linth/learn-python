'''
學習如何使用兩個 threads 



Reference:
    - https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
'''
import threading
import time


def sub_task():
    for i in range(5):
        print('child thread: ',  i)
        time.sleep(1)


if __name__ == '__main__':
    
    sub_t = threading.Thread(target=sub_task)
    sub_t.start()
    
    sub_t2 = threading.Thread(target=sub_task)
    sub_t2.start()
        
    sub_t.join() # 等待 sub_t 這個子執行緒結束
    sub_t2.join() # 等待 sub_t2 這個子執行緒結束
    
    print('Done.')


