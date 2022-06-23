'''
downloading file 範例: (使用 multi-thread class寫法)
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


# 使用 class-based 寫法 (請記得繼承 Thread class)
class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print(f'start downloading... {self._filename}')
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print(f'{self._filename} downloading finished! spend {time_to_download} time.')



# class-based 寫法
@cal_spend_time
def main_class_based():
    t1 = DownloadTask('Python.pdf')
    t1.start()

    t2 = DownloadTask('Peking Hot.avi')
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    # class-based 寫法
    main_class_based()
    