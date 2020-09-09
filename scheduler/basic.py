import sched
import time
from datetime import datetime


def show_time(*args, **kwargs):
    # print(f'Time: {time.time()}')
    print('datetime: ', datetime.now())
    print('args: ', args)
    print('kwargs: ', kwargs)


def show_time2():
    # print(f'Time2: {time.time()}')
    print('datetime: ', datetime.now())


def main():
    s = sched.scheduler(time.time, time.sleep)
    s2 = sched.scheduler(time.time, time.sleep)

    a = [1, 2, 3]
    d1 = {'dict': 'd1', }
    d2 = {'dict': 'd2', }

    s.enter(5, 2, show_time, argument=a)
    s.enter(10, 2, show_time, kwargs=d1)
    s.enter(10, 1, show_time2)

    s2.enter(5, 1, show_time, kwargs=d2)

    s.run()
    s2.run()


if __name__ == '__main__':
    main()
