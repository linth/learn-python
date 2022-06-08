'''
decorator 一般模板
    - 沒有規定要怎麼寫，所以只是提供參考。

'''

def decorator(fun, *arg, **kwargs):
    ''' 第一層裝飾器名稱 '''
    
    def wrapper(*args, **kwargs):
        ''' inner function. '''
        
        # 從這裡增加程式碼
        
        fun()
        
        # 從這裡增加程式碼
    return wrapper

@decorator
def show_hello():
    print('hello')


if __name__ == '__main__':
    show_hello()
    