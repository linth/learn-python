'''
Reference:
    - https://www.geeksforgeeks.org/class-as-decorator-in-python/
'''
import time


class Timer:
    def __init__(self, func):
        self.func = func

    ''' 使用Timer class當作decorator '''
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        res = self.func(*args, **kwargs)
        end_time = time.time()
        print('The executing time = {}'.format(end_time - start_time))
        return res


@Timer
def add(x, y):
    return x + y


@Timer
def mul():
    num_sum = 0
    for i in range(10000):
        num_sum = i + num_sum
    print('The totoal sum is {}'.format(num_sum))
    return num_sum


@Timer
def delay_function(delay):
    time.sleep(delay)


if __name__ == '__main__':
    ''' Results:
        The executing time = 0.0
        The result of add function is = 3
        The totoal sum is 49995000
        The executing time = 0.000997304916381836
        The result of mul function is = 49995000
        The executing time = 3.0002691745758057
    '''
    print('The result of add function is = {}'.format(add(1, 2)))
    print('The result of mul function is = {}'.format(mul()))

    delay_function(3)
