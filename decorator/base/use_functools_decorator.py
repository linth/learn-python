'''
使用 functools 來寫 decorator 
    - 沒有規定要怎麼寫，所以只是提供參考。
    - 可以搭配 decorator_template 比較差異。

結論:
    - 在裝飾器函式定義新的 function 並增加 @functools.wraps(fun)
    - 在 function 上使用 @decorator 

Reference:
    - https://www.twblogs.net/a/5cfdeb82bd9eee14029ec1fa
'''
import functools


def decorator(fun, *arg, **kwargs):
    ''' 第一層裝飾器名稱 '''
    print('arg 1', arg)
    print('kwargs 1', kwargs)
    
    @functools.wraps(fun)
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
    