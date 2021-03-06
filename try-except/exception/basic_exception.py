

class IeBaseException(Exception):
    """ the basic exception. """
    def __init__(self, class_name, function_name, msg=None, code=None):
        self.class_name = class_name
        self.function_name = function_name
        self.message = msg
        self.status_code = code


class GeneralException(IeBaseException):
    """ the general exception, please use it based on general situation or you aren't sure. """
    def __init__(self, class_name=None, function_name=None, msg=None, code=None):
        super().__init__(class_name, function_name, msg, code)


class DataException(IeBaseException):
    """ the data exception is for checking the form, model, and so on. """
    def __init__(self, class_name=None, function_name=None, msg=None, code=None):
        super().__init__(class_name, function_name, msg, code)


class ResponseFailureException(IeBaseException):
    """ the exception is for checking the Http response. """
    def __init__(self, class_name=None, function_name=None, msg=None, code=None):
        super().__init__(class_name, function_name, msg, code)