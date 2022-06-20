'''
兩個list使用 for-loop範例
    - 用zip()會傳回一個新的list, 也就是會需要使用額外的記憶體

Reference:
    - https://pythonnote.wordpress.com/2014/04/03/python%E6%8A%80%E5%B7%A7%E6%BC%82%E4%BA%AE%E5%8F%88%E9%80%9A%E9%A0%86%E7%9A%84%E7%A8%8B%E5%BC%8F%E7%A2%BC/
'''


names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

for name, color in zip(names, colors):
    print('name', name)
    print('color', color)
    

# for name, color in izip(names, colors):
#     print('name', name)
#     print('color', color)