'''
函式(Function)變數範圍(Scope)
    - 全域變數(Global Variable)
    - 只有在函式內才可以進行存取

! 非必要避免在函式中修改全域變數的值，因為永遠不會知道程式的其他地方有沒有使用了這個全域變數來進行運算。
! 而在函式中修改了它的值後，容易導致程式的副作用(Side Effect)或錯誤(Bug)。
    
Reference:
    - https://www.learncodewithmike.com/2019/12/python-function.html

'''

# 全域變數
x = 100

def cal_number():
    global x

    # 區域變數
    x = 20
    
    
if __name__ == '__main__':
    cal_number()
    
    print(x) # 全域變數
    