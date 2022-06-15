'''
callback function:
    - sum of two numbers.


Reference:
    - https://www.youtube.com/watch?v=iUrUf5ijiWs

'''

def add(n1, n2, cb):
    return cb(n1+n2)


def handle(result):
    # use english to show your result.
    print('result', result)
    
    
def handle2(result):
    print('結果是', result)
    
    
    
if __name__ == '__main__':
    
    add(4, 3, handle)
    add(5, 6, handle)
    
    add(4, 3, handle2)
    add(5, 6, handle2)
    