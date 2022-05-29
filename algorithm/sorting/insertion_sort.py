"""
Insertion Sort (插入排序法)
    - 

Reference:
    - https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm#
"""

def insertion_sort(list):
    for i in range(1, len(list)): # 從第二個 index 開始
        print(i)
        
        j = i-1
        next_element = list[i] # 下一個 element
        
        while (list[j] > next_element) and j>=0:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = next_element


def insertion_sort2(list):
    for i in range(1, len(list)+1): # 從第二個 index 開始
        print(i)
        
        j = i-1
        next_element = list[i] # 下一個 element
        
        while (list[j] > next_element):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = next_element
        

if __name__ == '__main__':
    list = [19, 2, 31, 45, 30, 11, 121, 27]
    insertion_sort(list)
    print(list)
    
    insertion_sort2(list)
    print(list)