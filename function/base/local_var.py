'''
函式(Function)變數範圍(Scope)
    - 區域變數(Local Variable)
    - 只有在函式內才可以進行存取
    
    
Reference:
    - https://www.learncodewithmike.com/2019/12/python-function.html
'''

def cal_number():
    
    # local variable.
    x = 100
    
    
if __name__ == '__main__':
    
    # print(x) # NameError: name 'x' is not defined
    
    cal_number()
    