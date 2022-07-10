'''
lambda + sorted 範例

    
Reference:
    - https://www.learncodewithmike.com/2019/12/python-lambda-functions.html
'''

cars = [
    ('mazda', 2000),
    ('toyota', 1000),
    ('benz', 5000)
]

print(sorted(cars)) # [('benz', 5000), ('mazda', 2000), ('toyota', 1000)]
print(sorted(cars, key=lambda car : car[1])) # [('toyota', 1000), ('mazda', 2000), ('benz', 5000)]
