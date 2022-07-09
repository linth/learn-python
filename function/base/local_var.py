'''
函式(Function)變數範圍(Scope)
    - 區域變數(Local Variable)
    - 只有在函式內才可以進行存取
    - 一般來說，全域變數是無法被該function scope內重新定義的變數進行存取。
    
    
Reference:
    - https://www.learncodewithmike.com/2019/12/python-function.html
'''

x = 1000


def cal_number():
    # local variable. x = 100 無法對 cal_number() 外的 x 重新賦值。
    x = 100
    
    
if __name__ == '__main__':
    
    print(x) # 1000
    
    