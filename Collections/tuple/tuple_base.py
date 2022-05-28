"""
Basic of tuple.
    - tuple 不允許修改
    - 但可以進行tuple組合
    - 不允許元素刪除，但可以刪除整個tuple
"""

t1 = (1, 2, 3)
t2 = ('george', 'mary', 40, 8)

print(t1)
print(t1[0])
print(t2)
print(t2[1], t2[1:])

# tuple 進行組合
print(t1 + t2)