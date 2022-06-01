'''
如何破解Python private members

Reference:
    - https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-1-private-member-on-python-fb5678b02582
'''

class Animal:
    def __init__(self):
        self.__alive = True 
        self.__age = 0
        
    def __print_something(self):
        print('call __print_something()')
        

if __name__ == '__main__':
    dog = Animal()
    print(dog._Animal__alive) # True
    
    res = dog._Animal__print_something() # call __print_something()
    
    