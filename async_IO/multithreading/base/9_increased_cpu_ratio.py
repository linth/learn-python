'''
如何使用 100% CPU資源? 
    - 必須要使用 multiple threads

Reference:
    - https://stackoverflow.com/questions/9244481/how-to-get-100-cpu-usage-from-a-c-program
'''

import time
import multiprocessing


if __name__ == '__main__':
    
    # how many cores for your computer?
    num_cpu = multiprocessing.cpu_count()
    print('number of cpu:', num_cpu)
    
    s = time.time()
    
    limit = 1000000
    primes = 0
    
    for num in range(limit):
        i = 2
        while i <= num:
            if num % i == 0:
                break
            i += 1
        
        if i == num:
            primes += 1
    
    e = time.time()
    
    print(e-s)