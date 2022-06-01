'''
protected function:
    - _ Single leading underscores.

Reference:
    - https://www.geeksforgeeks.org/private-variables-python/?ref=gcse

'''

class InfoData:
    def __init__(self, error=None):
        self._error = error
        self._type_of_error = None
        return self
    
    def _get_information(self):
        if self._error is None:
            return 'no error information.'
        return self._error
    
    def _set_type(self, type_input):
        self._type_of_error = type_input
        return self
                
        
class WebInfo(InfoData):
    def __init__(self, error=None):
        super().__init__(error)
        
        
        
        
if __name__ == '__main__':
    w = WebInfo('button cannot be used.') \
        ._set_type(400)
    
    # 當宣告成 protected，只能讓繼承的 class 進行使用。
    print(w._error)
    print(w._type_of_error)
    