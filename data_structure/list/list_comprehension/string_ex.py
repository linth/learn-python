'''

Reference:
    - https://www.youtube.com/watch?v=SNq4C988FjU&t=569s
'''

my_string = 'HelloMyNameIsGeorge'


my_string = [i for i in my_string]
print(my_string) # ['H', 'e', 'l', 'l', 'o', 'M', 'y', 'N', 'a', 'm', 'e', 'I', 's', 'G', 'e', 'o', 'r', 'g', 'e']



my_string = ''.join([i for i in my_string])
print(my_string) # HelloMyNameIsGeorge


# 推薦使用方法
my_string = ''.join(
    [i if i.islower() else ' ' + i for i in my_string]
)[1:]

print(my_string)

