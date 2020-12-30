"""
Reference:
    - https://docs.python.org/3/library/typing.html

Note:
    - Note The Python runtime does not enforce function and variable type annotations.
    They can be used by third party tools such as type checkers, IDEs, linters, etc.

Keyword:
    - Type aliases (類別別名)
"""
from typing import List
from typing import Dict, Tuple, Sequence
from typing import NewType

Vector = List[float]
ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


print(Vector) # typing.List[float]
print(type(Vector)) # <class 'typing.GenericMeta'>

new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector) # [2.0, -8.4, 10.8]
print(type(new_vector)) # <class 'list'>


def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    """ this is a example for type aliases. """
    pass


def broadcast_message_improved(message: str, servers: Sequence[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:
    """ we can use tuple, dict, list, sequence to compose them. """
    pass
