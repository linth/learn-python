'''
學習如何使用 queue + threads


Reference:
    - https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
'''
from threading import Thread
import time
import queue


class Worker(Thread):
    def __init__(self, queue, num):
        Thread.__init__(self)
        self.queue = queue
        self.num = num
    
    def run(self):
        while self.queue.qsize() > 0:
            # 取得新的資料
            msg = self.queue.get()
            
            # 處理資料
            print('worker:', self.num, msg)
            time.sleep(1)
            

if __name__ == '__main__':
    # 建立佇列
    q = queue.Queue()
    
    # 將資料放入佇列
    for i in range(10):
        q.put(f'Data {i}')
    
    # 建立 worker
    w1 = Worker(q, 1)
    w2 = Worker(q, 2)
    
    # worker 處理資料
    w1.start()
    w2.start()
    
    # 等待 worker 結束
    w1.join()
    w2.join()
    
    print('finished !!!')
    