'''
coroutines using yield.


Reference:
    - https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb
'''

def print_name(prefix):
    print('searching prefix: ', prefix)
    
    try:
        while True:
            print('yield: ', (yield))
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print('closing coroutine !!')
        
        
c = print_name('Dear')
c.__next__()
c.send('James')
c.send('Dear James')
c.close()
