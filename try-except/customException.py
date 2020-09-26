"""
Reference
    - https://github.com/parse-community/Parse-SDK-Android/blob/master/parse/src/main/java/com/parse/ParseException.java
    - https://franklingu.github.io/programming/2016/06/30/properly-reraise-exception-in-python/

Note:
    - 1) define error code with dictionary.
    - 2) create custom exception class to setup error message or status code what you get.
    - 3)
"""
# define the error code for denoting the error issue.
error_code = {
    "DIVISION_BY_ZERO": 100,
    "CONNECTION_FAILED": 101,
    "OBJECT_NOT_FOUND": 102,
    "INVALID_QUERY": 103,
    "GENERAL_ERROR": 104,
}


class MyCustomException(Exception):
    """ create a new custom exception what you want. """
    def __init__(self, error_msg: str, code=None):
        """
        set up the error_message and status code.
        :param error_msg: error message.
        :param code: status code for error.
        """
        self._error_message = error_msg
        self._status_code = code
        # TODO: we can use logging module to record the event and error message.


def foo():
    a = 1
    b = 0
    return a / b


def main():
    """
    execute a example: foo() to getting and handling the error exception.
    :return:
    """
    try:
        foo()
    except ZeroDivisionError as e:
        # [NOTE]: the class should be immutable because it cannot be modified to another value.
        print(f'error message: {e}; '
              f'status code: {100}')
        raise MyCustomException(e, error_code['DIVISION_BY_ZERO'])
    except Exception as e:
        raise MyCustomException(e, error_code['GENERAL_ERROR'])


if __name__ == '__main__':
    main()  # error message: division by zero; status code: 100
