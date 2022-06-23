'''
downloading file: (沒使用 multi-processing 的方式)
    - 使用兩個下載任務，由於沒有使用 multi-processing，任務會逐一一個一個完成，總共耗費時間將會是兩任務的總和。
    

Reference:
    - https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/13.%E8%BF%9B%E7%A8%8B%E5%92%8C%E7%BA%BF%E7%A8%8B.md
'''
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
    print(f'start downloading... {filename}')
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print(f'{filename} downloading finished! spend {time_to_download} time.')


@cal_spend_time
def main():
    download_task('Python.pdf')
    download_task('Peking Hot.avi')


if __name__ == '__main__':
    main()
    
    