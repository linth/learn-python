'''
callback function


Reference:
    - https://www.youtube.com/watch?v=iUrUf5ijiWs
'''

def test(arg):
    print(arg) # <function handle at 0x0000017126140700>
    
    # call callback function.
    arg() # 100
    

# define callback function.
def handle():
    print(100)
    

if __name__ == '__main__':
    
    test(handle)
    
    