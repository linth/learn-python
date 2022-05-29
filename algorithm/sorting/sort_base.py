"""
List sorting.
    - sorted: 原本的 list 則不受影響
    - sort: 改變原本的 list 內容
    - sorted(x, revere=True) 反向排序
    - itemgetter(), attrgetter()

Reference:
    - https://officeguide.cc/python-sort-sorted-tutorial-examples/
"""
from operator import itemgetter, attrgetter

scores = [
    ('Jane', 'B', 12),
    ('John', 'A', 15),
    ('Dave', 'B', 11)
]

if __name__ == '__main__':
    x = [4, 2, 5, 3, 1]
    
    # sorted: 原本的 list 則不受影響
    y = sorted(x)
    print(y)
    
    # sort: 改變原本的 list 內容
    print(x)
    x.sort()
    print(x)
    
    # 反向排序
    y = sorted(x, reverse=True)
    print(y)

    # 依照第三個數字元素排序
    print(sorted(scores, key=lambda s : s[2])) # [('Dave', 'B', 11), ('Jane', 'B', 12), ('John', 'A', 15)]
    # 以第二個元素排序，若相同則以第三個元素排序
    print(sorted(scores, key=itemgetter(1, 2)))
    