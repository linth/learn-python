'''
enum 範例
    - 總共定義4個枚舉類: enum, intenum, flag, intflag
    - 定義一個裝飾器: unique()
    - 定義一個輔助類: auto


Reference:
    - https://blog.louie.lu/2017/08/02/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-07-enum/
'''
from enum import Enum, IntEnum


class LightSwitch(Enum):
    OPNE = 'on'
    CLOSE = 'off'


class Animal(IntEnum):
    DOG = 1
    CAT = 2
    PANDA = 3
    



ls = LightSwitch('on')

print(ls) # LightSwitch.OPNE
print(ls.name) # OPEN
print(ls.value) # on


a = Animal.DOG
print(a) # Animal.DOG
