'''
References:
    - https://blog.louie.lu/2017/08/08/outdate-python-string-format-and-fstring/
'''


# using %-formatting.
def show_hello_word():
    s = 'Hello world'
    weight = 55.8
    print('This function is for showing the %s.' % s)
    print('There are two numbers: %d, %d.' % (10, 20))
    print('The weight of student is %.2f.' % weight)


# using  format.
def show_student_information():
    age = 35
    student_name = 'george'
    print('The information of student: name: {0}; age: {1}.'.format(student_name, age))


# using f-string. (Literal String Interpolation)
def show_info():
    age = 35
    student_name = 'george'
    weight = 78
    height = 180
    print(f'Name: {student_name.upper()}, Age: {age}, Weight: {weight}, Height: {height}')

show_hello_word()
show_student_information()
show_info()
