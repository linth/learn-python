import functools
import time

'''
執行函式所耗費的時間

References:
    - https://realpython.com/primer-on-python-decorators/
'''


def timer(func):
    # Print the runtime of the decorated function.
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        # print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


if __name__ == '__main__':
    waste_some_time(1)
    waste_some_time(999)
