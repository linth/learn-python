'''
Inner function:
    - 在 function 內，定義另一個 function。
    - inner function 有點類似 decorator
    - 需要知道閉包 (closures) 觀念

結論:
    - inner function 無法修改 global variable
    - inner function 如果要修改 outside function 則需要使用 nonlocal

References:
    - https://realpython.com/primer-on-python-decorators/
    - https://pythonexamples.org/python-inner-functions/
    - https://www.geeksforgeeks.org/python-inner-functions/
'''

def outside_function(txt):
    text = txt
    
    def inner_function():
        name = 'inner function.'
        x = 10
        # inner function 可以抓取外部變數
        print('text', text)
        
    inner_function()
    
    # 外部函數無法抓取 inner function.
    # print(name)
    

def function():
    
    print(f'inside the function...')

    def inner_function1():
        print(f'inner function 1.')

    def inner_function2():
        print(f'inner function 2.')

    inner_function1()
    inner_function2()


def IeJob(num):
    
    print(f'Go into the IeJob() function...')

    def print_hello():
        print(f'hello by print_hello() function.')

    def print_world():
        print(f'world by print_world() function.')

    def is_less_than_four() -> tuple:
        res_ = []
        if num >= 4:
            res_.append(num)
            res_.append(num**2)
        else:
            res_.append(f'less than 4')
            res_.append(num*2)
        return res_

    print_hello()
    print_world()
    return is_less_than_four()


# TODO: simple decorators.
def my_decorator(func):
    def wrapper():
        print('before the function is called.')
        func()
        print('after the function is called.')
    return wrapper


@my_decorator
def say_whee():
    print('Whee........')


# say_whee = my_decorator(say_whee) # without syntactic sugar.

if __name__ == '__main__':
    # parent(1)

    # say_whee()
    function()

    res = IeJob(3)
    print(f'input value: {res[0]}; the result: {res[1]}')
    
    print('------------------------')
    outf = outside_function('hi, everyone.')
    
    # 可以使用 dir 查詢的函數資訊 
    print(dir(outf))
    
    # 若想知道閉包儲存多少物件，可以印出__closure__屬性查看資訊，__closure__會是一個唯讀屬性；印出的資料型態是tuple。
    # TODO: 似乎沒有此 function. 