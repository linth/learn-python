from urllib.parse import parse_qs


# TODO: try to create a single-line expressions function to help us.
def get_parm_value():
    my_values = parse_qs('red=5&blue=0&green=',)
    print(my_values)

    print('Red: {}'.format(my_values.get('red')))
    print('Blue: {}'.format(my_values.get('blue')))
    print('Green: {}'.format(my_values.get('green')))

    red = my_values.get('red', [''])[0] or 0
    blue = my_values.get('blue', [''])[0] or 0
    green = my_values.get('green', [''])[0] or 0
    print(red, blue, green)


if __name__ == '__main__':
    get_parm_value()
