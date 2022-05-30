
# example 1: compare with two ages of human.
a = 22
b = 50

if a > b:
    print('the age of a: {} is larger than b: {}'.format(a, b))
elif a == b:
    print('the age of a: {} equals to b: {}'.format(a, b))
else:
    print('the age of a: {} is less than b: {}'.format(a, b))

# short hand if
# if a > b: print('the age of a: {} is larger than b: {}'.format(a, b))
# elif a == b: print('the age of a: {} equals to b: {}'.format(a, b))
# else: print('the age of a: {} is less than b: {}'.format(a, b))


# example 2: check the argrument is in the range (22 to 50) or not.
def check_number_range(num):
    if num >= 22 and num <= b:
        print('the number: {} is in the range (22 to 50)'.format(num))
    else:
        print('the number: {} isn\'t in the range (22 to 50)'.format(num))

check_number_range(44)
check_number_range(20)
check_number_range(100)

# example 3: 
