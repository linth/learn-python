'''
List comprehension
    - 學習不同寫法


Reference:
    - https://www.youtube.com/watch?v=SNq4C988FjU
'''
import time


fruits = ['apples', 'bananas', 'strawberries']


def list_used_direct():
    for fruit in fruits:
        # print(fruit)
        fruit = fruit.upper()

    #! 不會被覆蓋
    print(fruits) # ['apples', 'bananas', 'strawberries']


# 方法 1
def use_new_list():
    new_fruits = []
    
    for fruit in fruits:
        fruit = fruit.upper()
        new_fruits.append(fruit)
        
    return new_fruits
        

# 方法 2
def use_list_comprehension():
    return [fruit.upper() for fruit in fruits]
    

list_used_direct()

print(use_new_list())
print(use_list_comprehension())
