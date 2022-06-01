'''
建立 getter/setter (自訂義)
    - 可以使用 @property 方式，請參考 `/property` 資料。

Reference:
    - https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-1-private-member-on-python-fb5678b02582

'''

class Animal:
    def __init__(self):
        self.__alive = True
        self.__age = 0
        
    def get_age(self):
        return self.__age
    
    def add_age(self):
        # 限制提供使用 add_age 去增加 age 值。
        self.__age += 1
        return self.__age
        
        

if __name__ == '__main__':
    dog = Animal()
    age = dog.get_age()
    print(age)
    
    age = dog.add_age()
    print(age)
    