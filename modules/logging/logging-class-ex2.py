'''
logging usage in class 


Reference:
  - https://github.com/blacklanternsecurity/TREVORspray/blob/trevorspray-v2/trevorspray/lib/util/threadpool.py
'''
import logging


log = logging.getLogger('this is a class A logger.')

class A:
    def __init__(self, id, name, age) -> None:
        self.id = id
        self.name = name        
        self.age = age
        
    def get_id(self) -> int: 
        if self.id == None:
            log.critical(f'there isn\'t id value. please re-check it.')
            return 0
        return self.id
      
    def do_something(self) -> None:
        log.info(f'ID: {self.id}, Name: {self.name}, Age: {self.age}, do_something.')
        

if __name__ == '__main__':
    a = A(None, 'george', 30)
    
    a.get_id()    
    a.do_something()
    


