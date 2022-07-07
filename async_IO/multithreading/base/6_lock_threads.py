'''
學習如何使用 lock + threads


Reference:
    - https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
'''
import threading
import time
from threading import Thread
import queue


class Worker(Thread):
    def __init__(self, queue, num, lock):
        Thread.__init__(self)
        self.queue = queue
        self.num = num
        self.lock = lock
    
    def run(self):
        while self.queue.qsize() > 0:
            # 取得新的資料
            msg = self.queue.get()
            
            # 取得 lock
            self.lock.acquire()
            print('lock acquired by worker', self.num)
            
            # 不能讓多個執行緒同時進的工作
            print('worker', self.num, msg)
            time.sleep(1)
            
            # 釋放 lock
            print('lock released by worker', self.num)
            self.lock.release()
            

if __name__ == '__main__':
    q = queue.Queue()
    
    for i in range(5):
        q.put('Data {i}')
        
    # 建立 lock
    lock = threading.Lock()
    
    w1 = Worker(q, 1, lock)
    w2 = Worker(q, 2, lock)
    
    w1.start()
    w2.start()
    
    w1.join()
    w2.join()
    
    print('finished !!!')
    
