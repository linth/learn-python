"""
Reference:
    - https://pymotw.com/3/signal/index.html
"""
import signal
import os
import time


def receive_signal(signum, stack):
    print('Received: ', signum)


# Register signal handlers
# signal.signal(signal.SIGUSR1, receive_signal)
# signal.signal(signal.SIGUSR2, receive_signal)


# Print the process ID so it can be used with 'kill'
# to send this program signals.
# print('My PID is:', os.getpid())


# while True:
#     print('Waiting...')
#     time.sleep(3)


def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError('couldn\'t open device!')


signal.signal(signal.SIGALRM, handler)
signal.alarm(5)


# https://www.youtube.com/watch?v=NvxI07dl7gY
# a = {'id': 5, 'username': 'george', 'email': 'linth@gmail.com'}
# b = {'id': 4, 'username': 'may', 'email': 'may@gmail.com'}
#
#
# print(f'a = {a}, type of a: {type(a)}')
# print(f'b = {b}, type of b: {type(b)}')
#
# b.update(a)
# print(f'b = {b}')
#
#
# def get_a(**a):
#     print(a.keys(), a.values())
#     for i in a:
#         print(i, )
#
#
# get_a(**a)
