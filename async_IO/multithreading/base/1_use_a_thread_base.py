'''
學習如何使用單一 thread 



Reference:
    - https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
'''
import threading
import time


def sub_task():
    for i in range(5):
        print('child thread: ', i, '; time:', time.time())
        time.sleep(1)


if __name__ == '__main__':
    
    sub_t = threading.Thread(target=sub_task)
    sub_t.start()
        
    sub_t.join() # 等待 sub_t 這個子執行緒結束
    print('Done.')


