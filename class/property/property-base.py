'''
set, get function in class.
    - 一般寫法就是增加 set, get, del 那些函數來提供開發者進行呼叫。
    - 可以使用 @property

Reference:
    - https://www.runoob.com/python/python-func-property.html
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208
'''
# 一般寫法 set, get 
class C(object):
    
    def __init__(self):
        self._x = None
        
    def get_x(self):
        return self._x
    
    def set_x(self, value):
        self._x = value
        
    def del_x(self):
        del self._x


class D(object):
    
    def __init__(self) -> None:
        self._z = None
        
    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, value):
        self._z = value
    
    @z.deleter
    def z(self):
        del self._z
        

c = C()
c.set_x(1)
print(c.get_x())

d = D()
print(d._z) # None
d.z = 1000
print(d._z) # 1000