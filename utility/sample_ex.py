

crypto_list = ['george', 'peter', 'mary']
crypto_str = ', '.join(crypto_list)
print('crypto_str: ', crypto_str)


poem = '''all that doth flow we cannot liquid name Or else \
        would fire and water be the same; 
        But that is liquid which is moist and wet
        Fire that property can never get. 
        So, that is good result. Haha...'''

res = poem.endswith('be the same;')
print('res', res)
print(poem.find('else')) # 找到第一次出現
print(poem.rfind('be')) # 找到最後一次出現
print(poem.count('that'))
print(poem.isalnum()) # porm是否只有字母與數字

