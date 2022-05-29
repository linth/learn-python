"""
Merge sorting (合併排序法)
    - 把一個 list 開始逐步拆成兩兩一組
    - 合併時候再逐步根據大小先後加入到新的 list裡面
    
    - Merge Sort屬於Divide and Conquer演算法
    - 把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)，如此便解決了原先的問題。
    
Reference:
    - https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm#
    - https://www.youtube.com/watch?v=C9Xes8wH6Co&t=125s
"""

def merge_sort(unsorted_list):
    """ 前半部分都是將 list 拆成多個小的 list. """
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    # 找出中間值
    middle_idx = len(unsorted_list) // 2
    
    # 拆分兩個左右 list
    left_list = unsorted_list[:middle_idx]
    right_list = unsorted_list[middle_idx:]
    
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
        
    return list(merge(left_list, right_list))
    
def merge(left_half, right_half):
    res = []
    
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])

    # 如果其中一個 list 已經排完
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half        
    return res
    

if __name__ == '__main__':
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(merge_sort(unsorted_list))
    