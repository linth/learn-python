'''
一般傳統 class 寫法
    - 思考一下，如果我們今天要實作一個 __str__ 功能，卻又不能修改 A class 裡面的東西
    - 我們應該怎麼做? 請參考下個範例
    

Reference:
    - https://github.com/twtrubiks/python-notes/tree/master/what_is_the_mixin
'''

class A:
    
    def __init__(self, x1, x2) -> None:
        self.x1 = x1
        self.x2 = x2
        

if __name__ == '__main__':
    a = A('x1', 'y1')
    print(a)
    