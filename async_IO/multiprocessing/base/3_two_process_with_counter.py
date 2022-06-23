'''
這範例就可以驗證各自 Process 皆獨立
    - 每個 Process 都有各自的參數，皆獨立。
    - 如果是要共用，可以使用 multiprocessing 模組中的 Queue 來處理。
    - 也可以使用 multi-thread 方式 (請參考)


Reference:
    - https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/13.%E8%BF%9B%E7%A8%8B%E5%92%8C%E7%BA%BF%E7%A8%8B.md
'''
from multiprocessing import Process
from time import sleep


counter = 0


def sub_task(string):
    global counter
    
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)
        

def main():
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    main() # PingPongPingPongPongPingPongPingPingPongPongPingPongPingPongPingPongPingPingPong
    