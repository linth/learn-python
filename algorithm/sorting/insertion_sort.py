"""
Insertion Sort (插入排序法)
    1. 順序從左到右開始
    2. 從剩下的array, 找出最小的數值
    3. 取最小值進行替換

Reference:
    - https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm#
"""

def insertion_sort(list):
    n = len(list)
    
    for i in range(1, n): # 從第二個 index 開始
        j = i-1
        next_element = list[i] # 抓下一個 element
        
        while (list[j] > next_element) and j>=0:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = next_element
       

if __name__ == '__main__':
    list = [19, 2, 31, 45, 30, 11, 121, 27]
    insertion_sort(list)
    print(list)
    