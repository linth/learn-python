

"""
class and property concept.

Reference:
    - https://medium.com/bryanyang0528/python-setter-%E5%92%8C-getter-6c08a9d37d46
"""


class gundam(object):

    def __init__(self, driver):
        self._driver = driver

    def get_driver(self):
        """ general get property function. """
        return self._driver

    def set_driver(self, new_driver):
        self._driver = new_driver

    @property
    def driver(self):
        """ using @property to get property. """
        return self._driver

    @driver.setter
    def driver(self, new_driver):
        """ another way to set up your property. """
        print('set the driver.')
        self._driver = new_driver


if __name__ == '__main__':
    g = gundam('Bryan')
    print(g.get_driver())
