'''
Closure(閉包)


Reference:
    - https://medium.com/tsungs-blog/python-%E4%BD%9C%E7%94%A8%E5%9F%9F%E8%88%87closure-%E9%96%89%E5%8C%85-18426536e25c

'''

def compare(m, n):
    return m if m > n else n


if __name__ == '__main__':
        
    # assign function 物件給 fun
    fun = compare
    
    print(compare) # <function compare at 0x00000210C126F1F0>
    print(fun) # <function compare at 0x00000210C126F1F0>
    print(fun(1,2))
    print(compare(1, 2))