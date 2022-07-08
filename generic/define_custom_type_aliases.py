'''
可自定義類別別名 (type aliases)


Reference:
    - https://docs.python.org/3.6/library/typing.html
'''
from typing import List, Dict, Tuple

Vector = List[float]

connection_option = Dict[str, str]
address = Tuple[str, int]
server = Tuple[address, connection_option]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


def set_information(co: connection_option, a: address):
    connection_option = co
    address = a
    print('server', server)
    return server


new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)

# TODO: 如何抓取內部資料?
res = set_information({'type', 'kao'}, ('address', 828146))
print('res', res, type(res))
