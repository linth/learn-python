'''
static method
    - 避免新加入的開發人員意外改變類別(Class)或物件(Object)的狀態。
    - 靜態方法(Static Method)在類別中是獨立的，所以有助於單元的測試。
    
    
Reference:
    - https://www.learncodewithmike.com/2020/01/python-method.html
'''

class Cars:
    
    # 靜態方法
    @staticmethod
    def accelerate():
        print("Accelerate is static method.") 
    
    @staticmethod
    def speed_rate(distance, minute):
        return distance / minute
    

# 透過物件呼叫
c = Cars()
c_rate = c.speed_rate(10000, 20)
print('vechicle rate (c): ', c_rate)


# 透過類別呼叫
c2 = Cars.speed_rate(20000, 20)
print('vehicle rate (2): ', c2)


'''Results:
vechicle rate (c):  500.0
vehicle rate (2):  1000.0
'''