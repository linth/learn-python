'''
callback function:
    - sum of two numbers.


Reference:
    - https://www.youtube.com/watch?v=iUrUf5ijiWs

'''

def add(n1, n2, cb):
    return cb(n1+n2)


def handle(result):
    print('result', result)
    
    
if __name__ == '__main__':
    add(4, 3, handle)
    
    add(5, 6, handle)
    