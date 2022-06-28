"""
基本的裝飾器寫法:
    - 可以參考 decorator_template.py

"""

def myDeco(callback):

    def run():
        
        print(f'call decorator function...')
        callback()
        print(f'end of decorator function...')
        
    return run


@myDeco
def test():
    print(f'call test() function...')


if __name__ == '__main__':
    test()
    
