'''
[建議] 擴展內建類型，如：list, string, dict, ..., etc 的正確方法是使用 collections 模組

需要注意：
    - 如果直接使用 list, dict等，可能會有些函數未被實做出來，造成不可預期的錯誤。

'''
from collections import UserList


# 不好的範例
class BadList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        
        if index % 2 == 0:
            prefix = 'even'
        else:
            prefix = 'odd'
        
        return f'[{prefix}] {value}'
    

# 好的範例
class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        
        if index % 2 == 0:
            prefix = 'even'
        else:
            prefix = 'odd'
        
        return f'[{prefix}] {value}'


if __name__ == '__main__':
    l = [0, 1, 2, 3, 4, 5]
    
    b_good = GoodList(l)
    print(b_good[0])
    print(b_good[1])
    print(' '.join(b_good))
    
    b = BadList(l)    
    print(b[0])
    print(b[1])
    print(''.join(b)) # TypeError: sequence item 0: expected str instance, int found
