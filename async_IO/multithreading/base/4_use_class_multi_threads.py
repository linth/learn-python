'''
學習如何使用 class-based threads


Reference:
    - https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
'''
from threading import Thread
import time


class FirstThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        print('thread', self.num)
        time.sleep(1)


if __name__ == '__main__':
    threads = []
    
    for i in range(5):
        threads.append(FirstThread(i))
        threads[i].start()
        
    for i in range(5):
        threads[i].join()
        
    print('Finished !!!')
    