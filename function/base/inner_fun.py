'''
Inner function:
    - 在 function 內，定義另一個 function。
    - inner function 有點類似 decorator
    - 需要知道閉包 (closures) 觀念

References:
    - https://realpython.com/primer-on-python-decorators/
    - https://pythonexamples.org/python-inner-functions/
    - https://www.geeksforgeeks.org/python-inner-functions/
'''

def outside_function(txt):
    text = txt
    
    def inner_function():
        print('text', text)
        
    inner_function()
    

def function():
    """
    Working of Inner Functions:
        Following is the step by step execution of the above program.

        1. Define function().
        2. Call function().
        3. Execute print('Inside the function.').
        4. Define innerFunction1().
        5. Define innerFunction2().
        6. Call innerFunction1().
        7. Execute print('Inner function 1.').
        8. Call innerFunction1().
        9. Execute print('Inner function 2.').

    :return:
    """
    print(f'inside the function...')

    def inner_function1():
        print(f'inner function 1.')

    def inner_function2():
        print(f'inner function 2.')

    inner_function1()
    inner_function2()


def IeJob(num):
    """
    可以使用在 function-based api 應用程式上面。
    :param num:
    :return:
    """
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
    outside_function('hi, everyone.')
