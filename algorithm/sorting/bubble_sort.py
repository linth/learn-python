"""
bubble sorting (氣泡排序法)
    - 兩兩比較，左邊數字大則交換，否則繼續。
    
Reference:
    - https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
"""

def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for idx in range(i):
            if list[idx] > list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
        
        
if __name__ == '__main__':
    list = [19, 2, 31, 45, 6, 11, 121, 27]
    bubble_sort(list)
    print(list)
    