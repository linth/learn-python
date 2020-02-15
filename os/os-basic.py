"""
Reference:
    - https://www.guru99.com/python-regular-expressions-complete-tutorial.html
"""

import re

arr_list = [
    'SCD-10000.pdf',
    'SCD-1192.pdf',
    'SCD-119222.pdf',
    'SCD-1193.pdf',
    'SCD-999.pdf',
    'test',
]


def example():
    query = input('please type keyword:\n')
    for i in arr_list:
        res = re.findall(query, i, re.I)

        if res:
            print(f'{i}')


if __name__ == '__main__':
    example()
