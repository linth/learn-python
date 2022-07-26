'''
class method:
    - 請注意跟 instance method 的範例進行比較差異。
    - 有@classmethod裝飾詞(Decorator)的方法(Method)
    - 被呼叫時，類別方法(Class Method)為cls參數
    
1. 類別方法(Class Method)僅能改變類別的狀態，而無法改變物件(Object)的狀態。
    - 因為它沒有self參數可以存取物件的屬性(Attribute)及方法(Method)
    
2. 
    

Reference:
    - https://www.learncodewithmike.com/2020/01/python-method.html
'''
class Cars:
    door = 4 # 類別屬性
    
    # 類別方法 (class method)
    @classmethod
    def open_door(cls):
        print(f'{cls} has {cls.door} doors.')
        
        

# 透過物件呼叫
c = Cars()
c.open_door() 

#透過類別呼叫
Cars.open_door()

'''Results:
<class '__main__.Cars'> has 4 doors.
<class '__main__.Cars'> has 4 doors.
'''
