"""
Reference
- https://github.com/parse-community/Parse-SDK-Android/blob/master/parse/src/main/java/com/parse/ParseException.java
- https://franklingu.github.io/programming/2016/06/30/properly-reraise-exception-in-python/
"""
# define the error code for denoting the error issue.
error_code = {
    "DIVISION_BY_ZERO": 100,
    "CONNECTION_FAILED": 101,
    "OBJECT_NOT_FOUND": 102,
    "INVALID_QUERY": 103,
}


# create a new custom exception what you want.
class MyCustomException(Exception):
    def __init__(self, e, num):
        """
        set up the error_message and status code.
        :param e: error message
        :param num: status code
        """
        self._error_message = e
        self._status_code = num
        # TODO: we can use logging module to record the event and error message.


def foo():
    a = 1
    b = 0
    return a / b


def main():
    try:
        foo()
    except ZeroDivisionError as e:
        # [NOTE]: the class should be immutable because it cannot be modified to another value.
        m = MyCustomException(e, error_code['DIVISION_BY_ZERO'])
        print(f'error message: {m._error_message}; '
              f'status code: {m._status_code}')
        raise MyCustomException(e, error_code['DIVISION_BY_ZERO'])


if __name__ == '__main__':
    main()  # error message: division by zero; status code: 100
