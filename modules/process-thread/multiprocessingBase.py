"""
Multiprocessing

Reference:
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064
"""
import os
from multiprocessing import Process


def run_proc(name):
    print(f'Run child process {name} ({os.getpid()})')


if __name__ == '__main__':
    # print(f'process {os.getpid()} starting...')
    # # only work on Unix/Linux/Mac.
    # pid = os.fork()
    # if pid == 0:
    #     print(f'I am child process {os.getpid()} and my parent is {os.getppid()}')
    # else:
    #     print(f'I {os.getpid()} just created a child process {pid}')

    print(f'Parent process {os.getpid()}')
    p = Process(target=run_proc, args=('test', ))
    print(f'Child process will start.')

    p.start()
    p.join()
    print(f'Child process end.')
