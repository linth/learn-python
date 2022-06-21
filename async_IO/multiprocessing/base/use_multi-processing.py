'''
downloading file:
    - 使用兩個下載任務，有使用 multi-processing，任務會放到不同的process中同時啟動，總共耗費時間將會是某項最長結果。
    - 請跟 not_use_multi-processing 範例進行比較。
    - 此範例使用兩個 process 來執行
    

Reference:
    - https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/13.%E8%BF%9B%E7%A8%8B%E5%92%8C%E7%BA%BF%E7%A8%8B.md
'''
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def cal_spend_time(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f'spend total time: ({end - start})')
    return wrapper


def download_task(filename):
    print('executing the process:', getpid())
    print(f'start downloading... {filename}')
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print(f'{filename} downloading finished! spend {time_to_download} time.')


@cal_spend_time
def main():    
    p1 = Process(target=download_task, args=('Python.pdf', ))
    p1.start()
    
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    
    p1.join()
    p2.join()
    

if __name__ == '__main__':
    main()
    
    
    