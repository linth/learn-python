'''
使用 multiple-threading 範例

Reference:
    - https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb
'''
from threading import Thread
import time


counter = 0


def print_cube(num):
    print(num * num * num)


def print_square(num):
    print(num * num)


if __name__ == '__main__':
    t1 = Thread(target=print_square, args=(10, ))
    t2 = Thread(target=print_cube, args=(10, ))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print('Done !!')

    
