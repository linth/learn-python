'''
[問題]
    - 若想在某個function中assign新的值給先前宣告在全域變數(global scope)中的變數時，一樣也會報UnboundLocalError錯誤訊息。


[解決方法]
    - 宣告nonlocal去操作captured variable。
    - 使用 `nonlocal`

Reference:
    - https://medium.com/tsungs-blog/python-%E4%BD%9C%E7%94%A8%E5%9F%9F%E8%88%87closure-%E9%96%89%E5%8C%85-18426536e25c

'''
x = 10

def student():
    
    height = 180
    weight = 70
    
    def show_information():
        # 使用 nonlocal
        nonlocal height
        nonlocal weight
        global x
        
        height += 1
        weight -= 1
        
        print('height', height) # 181
        print('weight', weight) # 69
        print('inner', x + 10) # 20
        
    return show_information # None

if __name__ == '__main__':
    s = student()
    
    print(s) # <function student.<locals>.show_information at 0x00000264D90D0670>
    print(s())
    '''
    height 181
    weight 69
    None -> show_information()
    ''' 