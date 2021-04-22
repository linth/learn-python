"""
Iteration and Recursion.

1) Iteration: 疊代法 (Iterative method)
    - 用迴圈去循環重複程式碼的某些部分來得到答案

2) Recursion: 遞迴法
    - 則是重複呼叫自身程式碼來得到答案。
    - Direct Recursion: 函式直接呼叫本身，稱為直接遞迴。
    - Indirect Recursion: 函式呼叫另外函式，再從另外函式呼叫原來的函式，稱為間接遞迴。


Reference:
    - http://simonsays-tw.com/web/Recursion/Iteration&Recursion.html
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017316949097888
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017323698112640
"""
from collections import Iterable


def factorial(n: int):
    answer = 1 # 0! = 1

    for i in range(1, n):
        answer *= i
    return n, answer


if __name__ == '__main__':
    l = [1, 2, 4]
    res = isinstance(l, Iterable)
    print(f'Is the object of l iterative? Ans: {res}')

    res2 = factorial(4)
    print(f'the values of {res2[0]} factorial: {res2[1]}')


