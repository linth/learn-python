

def comparing_equality():
    """ when object copy is equal but not identical. """
    a = [1, 2, 3]
    b = a.copy()
    print(a)
    print(b)

    print(a == b) # True, because both objects have the same value.
    print(a is b) # False, that means these variables are in different memory addresses.

    # the function of id() is to get the address of memory.
    print(f'a = {id(a)}, b = {id(b)}')


def situation_1():
    """ The situation is that Python use the same memory to put the variable because of optimization. """
    parms_c = 1
    parms_d = 1
    print(f'the memory address of parameter c is equals to {id(parms_c)}, and the memory address of parameter d is equals to {id(parms_d)}')

    if parms_c is parms_d:
        print('yes, they are the same.')
    else:
        print('no, they are not the same.')


if __name__ == '__main__':
    comparing_equality()

    situation_1()



