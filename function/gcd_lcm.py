'''
最大工因數、最小公倍數
    - 最大工因數: 找出都可以整除於兩個數，最後將這些數字相乘
    
    - 最小公倍數: 找出都可以整除於兩個數，最後全部數相乘。


Reference:
    - https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/06.%E5%87%BD%E6%95%B0%E5%92%8C%E6%A8%A1%E5%9D%97%E7%9A%84%E4%BD%BF%E7%94%A8.md
    - https://www.youtube.com/watch?v=IikEWljfL94
'''

# 最大工因數
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
        

# 最小公倍數
def lcm(x, y):
    return x * y // gcd(x, y)
    

print(gcd(10, 30)) # 10
print(lcm(10, 30)) # 30