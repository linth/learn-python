'''
downloading file 範例: (使用 multi-thread function寫法)
    - 使用兩個下載任務，有使用 multi-thread，任務會放到不同的 thread 中同時啟動，總共耗費時間將會是某項最長結果。
    - 請跟 use_multi-processing 範例進行比較。
    - 此範例使用兩個 thread 來執行，以及各實作 class-based and function-based 方式。
    - 多 thread 程式可以共享記憶體資源


Reference:
    - https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/13.%E8%BF%9B%E7%A8%8B%E5%92%8C%E7%BA%BF%E7%A8%8B.md
'''
from random import randint
from threading import Thread
from time import time, sleep


def cal_spend_time(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f'spend total time: ({end - start})')
    return wrapper


# 使用 function-based 寫法
def download_task(filename):
    print(f'start downloading... {filename}')
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print(f'{filename} downloading finished! spend {time_to_download} time.')



# function-based 寫法    
@cal_spend_time
def main():    
    p1 = Thread(target=download_task, args=('Python.pdf', ))
    p1.start()

    p2 = Thread(target=download_task, args=('Peking Hot.avi', ))
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':    
    # function-based 寫法
    main()
