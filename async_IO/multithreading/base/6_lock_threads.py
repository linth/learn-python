'''
學習如何使用 lock + threads
    - 在平行化的多執行緒程式中，每個執行緒都是同時在執行的，若遇到不可以讓多個執行緒同時進行的工作時（例如將資料寫入同一個檔案），就必須使用鎖定（lock）的方式，一次只讓一個執行緒處理這種工作。

    - 當一個執行緒呼叫了 Lock 的 acquire 時，代表取得了這個 Lock 的使用權，接著它就可以往下執行裡面的工作，若此時又有另外一個執行緒想要呼叫 acquire 取得使用權的話，就必須等待上一個執行緒執行完，並呼叫 release 釋放這個 Lock 之後，才能夠取得這個 Lock 的使用權，接著執行裡面的工作。
    - 在這種狀況下雖然兩個 Worker 是同時執行的，但是由於 Lock 的互斥作用，因此可以確保被 Lock 的 acquire 與 release 包起來的這段程式碼不會被兩個執行緒同時執行。
    
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
    
