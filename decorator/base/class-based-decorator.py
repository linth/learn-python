'''
Class-based decorator

Reference:
    - https://medium.com/tsungs-blog/%E6%B7%BA%E8%AB%87-python-%E4%B8%AD%E7%9A%84decorator-%E4%B8%8B-c8b750ec6daf
'''

# Decorator Class Sample
class decorator(object):

    def __init__(self, f):
        print('enter init')
        self.f = f
        print('exit init')

    def __call__(self, *args, **kwargs):
        print("Entering", self.f.__name__)
        r = self.f(*args, **kwargs)
        print("Exited", self.f.__name__)
        return r

print('start decorator ')

@decorator
def hello(k):
    print('inside hello')
    return("k is: " + k)

print('excute')
print(hello('say hello!'))