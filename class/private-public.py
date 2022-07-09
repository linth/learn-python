'''
private/public attribute.
    - private: __ 雙底線
    - _ 單底線
    

Reference:
    - https://medium.com/ai%E5%8F%8D%E6%96%97%E5%9F%8E/python-%E5%BA%95%E7%B7%9A-%E4%BB%8B%E7%B4%B9-%E8%BD%89%E9%8C%84-5b0349efdf52
'''

class A:
    
    __z = 3
    
    def __init__(self, x, y):
        self._x = x
        self.__y = y
    
    def get_x(self):
        return self._x
        

if __name__ == '__main__':
    a = A(1, 2)
    print(a.get_x()) # 1
    print(a._x) # 1
    # print(a.__y) # AttributeError: 'A' object has no attribute '__y'
    
    
    #! 雖然使用 __ 雙底線來保護資料，但依舊還是可以抓取。
    print(a._A__z) 
    print(a._A__y)