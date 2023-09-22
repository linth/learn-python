"""
Logging modules.

Reference:
    - https://docs.python.org/zh-cn/3/howto/logging.html
    - https://www.youtube.com/watch?v=-ARI4Cz-awo&t=125s
"""
import logging

logging.basicConfig(
    filename='example1.log', 
    encoding='utf-8',
    level=logging.DEBUG
  )

class Calculating:
  
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
  
    def add(self, x, y):
        self.logger.debug('The function: add is executing.')
        return x + y

    def subtract(self, x, y):
        self.logger.debug('The function: subtract is executing.')
        return x - y

    def multiply(self, x, y):
        self.logger.debug('The function: multiply is executing.')
        return x * y

    def divide(self, x, y):
        self.logger.debug('The function: divide is executing.')
        return x / y


    def example1(self):
        """
        example 1: print information based on your setting level.
        :return:
        """
        # logging.basicConfig(filename='example1.log', level=logging.DEBUG)

        self.logger.debug('the message should go to the log file.')
        self.logger.info('So should this')
        self.logger.warning('And this, too')


    def example2(self):
        # logging.basicConfig(filename='example2.log', level=logging.DEBUG)

        num1, num2 = 10, 5
        add_result = self.add(num1, num2)
        subtract_result = self.subtract(num1, num2)
        multiply_result = self.multiply(num1, num2)
        divide_result = self.divide(num1, num2)
        
        print(add_result)
        print(subtract_result)
        print(multiply_result)
        print(divide_result)


if __name__ == '__main__':
    # example1()
    # example2()
    c = Calculating()
    c.example1()
    c.example2()
