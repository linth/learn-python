'''
decorator 一般模板
    - 沒有規定要怎麼寫，所以只是提供參考。

'''

def decorator(fun):
    ''' 第一層裝飾器名稱 '''
    
    def wrapper(*args, **kwargs):
        ''' inner function. '''
        
        # 從這裡增加程式碼
        
        fun()
        
        # 從這裡增加程式碼
    return wrapper

def show_hello():
    print('hello')


if __name__ == '__main__':
    decorator(show_hello())
    