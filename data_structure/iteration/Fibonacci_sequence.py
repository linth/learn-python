"""
Fibonacci sequence
    - [0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181]

Reference:
    - https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
"""

def fib(n: int):
    # use reursive
    if n <= 2:
        return 1
    
    return fib(n-1) + fib(n-2)

def fib2(n: int):
    # use reursive
    if n <= 2:
        return 1
    
    return fib(n+1) - fib(n-1)

def fib3(n: int): # n is index.
    print('how many numbers:', n)
    
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    prev, curr = 0, 1
    two_sum = 0
    
    for i in range(3, n+1): # [0, 1, 1, 2, 3, 5, ..., ]
        two_sum = prev + curr
        prev, curr = curr, two_sum
    return two_sum


def fib4(n: int) -> list:
    # 想要創建一個可以 return fib list.
    prev, curr = 0, 1
    
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    if n > 2:
        res = [0, 1]
        for i in range(3, n+1):
            res.append(prev + curr)
            prev, curr = curr, prev+curr
    return res   
    

if __name__ == '__main__':
    # print(fib(7))
    
    # print(fib2(10))
    
    print(fib3(10))
    
    
    