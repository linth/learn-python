"""
selection sorting algorithm.

1. 順序從左到右開始
2. 從剩下的array, 找出最小的數值
3. 取最小值進行替換

Reference:
    - https://www.geeksforgeeks.org/python-program-for-selection-sort/?ref=gcse
"""

def selection_sort(a: list):
    n = len(a)
    
    for i in range(n):
        # find the minimum element in the ramaining unsorted array.
        min_idx = i
        
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def selection_sort2(a: list):
    """ 改善上面的寫法 """
    n = len(a)
    
    for i in range(n):
        min_idx = i
        
    for j in range(min_idx+1, n):
        if a[min_idx] > a[j]:
            min_idx = j
        a[j], a[min_idx] = a[min_idx], a[j]
    return a

if __name__ == '__main__':
    arr = [2, 3, 1, 6, 9, 11, 5]
    res = selection_sort(arr)
    print(f'after sorting, the result = {res}')
    
    res2 = selection_sort2(arr)
    print(f'after sorting, the result2 = {res2}')
    