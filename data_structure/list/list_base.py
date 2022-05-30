"""
Basic of list
    - append
    - del
    - pop
    - [0] * 4 = [0, 0, 0, 0]
    - len
    - max, min
"""

# def compare():
#     list1 = [1, 3, 4, 6]
#     list2 = [1, 6, 7, 10]

#     return (list1 > list2) - (list1 < list2)

if __name__ == '__main__':
    list = []

    list.append(1)
    list.append(4)
    list.append(5)
    list.append(8)
    list.append(13)

    print(list)
    print(list[:2]) # 最後面一個數字要減一, [1, 4]
    del list[0]
    print(list)
    print(max(list))
    