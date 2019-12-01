"""
References:
    - https://realpython.com/python-logging/
    - https://medium.com/@galea/python-logging-example-with-color-formatting-file-handlers-6ee21d363184
"""
import logging
import coloredlogs


def run_print():
    pass


if __name__ == '__main__':
    logger = logging.getLogger('your-module')
    logger.info('running hello world module...')
    run_print()
