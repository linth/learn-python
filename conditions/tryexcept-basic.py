# try except for python.

# example 1: check the number is odd or even.
# input = int(input('please type a number: '))
# if input % 2 == 0:
#     print('{} is a even'.format(input))
# else:
#     print('{} is a odd'.format(input))

# short hand if
# print('{0} is a {1}'.format(input, 'odd' if input % 2 != 0 else 'even'))

try:
    input = int(input('please type a number: '))
    print('{0} is a {1}'.format(input, 'odd' if input % 2 != 0 else 'even'))
except ValueError: # check the type of input.
    print('please type a number: <\'int\'>, thank you.')
except (EOFError, KeyboardInterrupt):
    print('interrupt the program.')
finally: # No matter what it must be executed.
    print('the end of program.')
