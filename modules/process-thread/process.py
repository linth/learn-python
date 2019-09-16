'''
References:
    -   https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064
'''
import os
from multiprocessing import Process

# def example():
#     print('Process start... {}'.format(os.getpid()))
#     pid = os.fork()
#
#     if pid == 0:
#         print('This is child process {} and my parent is {}'.format(os.getpid(), os.getppid()))
#     else:
#         print('{} create a child process {}'.format(os.getpid(), pid))

def run_process(name):
    print('Run child process {} {}...'.format(name, os.getpid()))


def main():
    print('Parent process {}'.format(os.getpid()))
    p = Process(target=run_process, args=('test',))

    print('The child process will start....')
    p.start() # 使用start啟動
    p.join()
    print('The child process is end.')

if __name__ == '__main__':
    main()
