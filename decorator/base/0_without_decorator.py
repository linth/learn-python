'''
不使用 decorator 會怎麼寫程式?

Reference:
    - https://medium.com/tsungs-blog/%E6%B7%BA%E8%AB%87-python-%E4%B8%AD%E7%9A%84decorator-%E4%B8%8A-d18a9375385a
'''

def print_my_name(name):
    print("My name is %s" %(name()))
    return name


def my_name():
    return "George"


name = print_my_name(my_name)
