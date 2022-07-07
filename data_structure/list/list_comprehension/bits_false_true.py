'''
False/True example.


Reference:
    - https://www.youtube.com/watch?v=SNq4C988FjU
'''

from re import T


bits = [False, True, False, False, True, False, False, True]


# 方法 1
def method1():
    new_bits = []

    for b in bits:
        if b == True:
            new_bits.append(1)
        else:
            new_bits.append(0)
    return new_bits


# 方法 2
def method2():
    return [1 if b == True else 0 for b in bits]



print(bits)
print(method1())
print(method2())
    
