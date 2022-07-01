'''
學習如何使用多個 threads 


Reference:
    - https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
'''
import threading
import time


def job(num):
    for i in range(2):
        print("Thread", num, '; number:', i)
        time.sleep(1)
  
  
if __name__ == '__main__':
    
    threads = []
    
    # 建立 5 個子執行緒，每個執行緒都會執行函式 job 任務。
    for i in range(5):
        threads.append(threading.Thread(target=job, args=(i,)))
        threads[i].start()
        
    
    for i in range(5):
        threads[i].join()
        
    print('finished !!!')
    