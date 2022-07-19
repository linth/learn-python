'''
Package 
    - 就是一個容器(資料夾)，包含了一個或多個的模組(Module)
    - 並且擁有__init__.py檔案，其中可以撰寫套件(Package)初始化的程式碼。

Reference:
    - https://www.learncodewithmike.com/2020/01/python-module-and-package.html
'''

class Post:
    
    def __init__(self):
        self.title = []
        
    def add_post(self, title):
        self.title.append(title)
        
    def delete_post(self, title):
        self.title.remove(title)
        
        
    