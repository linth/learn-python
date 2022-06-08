'''
函式(Function)變數範圍(Scope)
    - 全域變數(Global Variable)
    - 只有在函式內才可以進行存取

! 非必要避免在函式中修改全域變數的值，因為永遠不會知道程式的其他地方有沒有使用了這個全域變數來進行運算。
! 而在函式中修改了它的值後，容易導致程式的副作用(Side Effect)或錯誤(Bug)。

結論:
    - inner function 無法修改 global variable
    - inner function 如果要修改 outside function 則需要使用 nonlocal


Reference:
    - https://www.learncodewithmike.com/2019/12/python-function.html
    - https://medium.com/tsungs-blog/python-%E4%BD%9C%E7%94%A8%E5%9F%9F%E8%88%87closure-%E9%96%89%E5%8C%85-18426536e25c

'''

# 全域變數
x = 100

def cal_number():
    global x

    # 區域變數
    x = 20
    
    def show_global_var():
        print('1) inner x:', x+10)
        # print(id(x+10))
        
    def set_global_var(global_var):
        print('2) inner x:', global_var+10)
        # print(id(global_var+10))
        
    show_global_var()
    set_global_var(x)
    
    print('out x', x)
    
    
if __name__ == '__main__':
    cal_number()
    
    print(x) # 全域變數
    
    ''' result:
    1) inner x: 30
    2) inner x: 30
    out x 20
    20
    '''
    