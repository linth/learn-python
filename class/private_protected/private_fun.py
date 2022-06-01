'''
private function:
    - __ double leading underscores.

Reference:
    - https://www.geeksforgeeks.org/private-variables-python/?ref=gcse

'''

class Geek:    
    def __double_method(self):
        print('show __double_method() by Geek')
        
    def show_double_method(self):
        print('execute show_double_method()')
        self.__double_method()
        
        
class Pyth(Geek):
    def __double_method(self):
        print('show __double_method() by Pyth')
        
        
        
if __name__ == '__main__':
    p = Pyth()
    
    # 當宣告成 private，無法直接在外部呼叫使用 (非特定 class 內)
    # p.__double_method() # AttributeError: 'Pyth' object has no attribute '__double_method'
    p.show_double_method()
    