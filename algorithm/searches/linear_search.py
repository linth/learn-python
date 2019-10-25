import math

'''
References:
    - https://www.geeksforgeeks.org/linear-search/
'''

# Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].
# example:
# Input : arr[] = {10, 20, 80, 30, 60, 50,
#                      110, 100, 130, 170}
#           x = 110;
# Output : 6
# Element x is present at index 6


def search(arr, n, x):

    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


if __name__ == '__main__':
    arr = [2, 11, 89, 40, 23, 8]
    x = 89
    n = len(arr)

    res = search(arr, n, x)
    if res == -1:
        print('Element is not present in array.')
    else:
        print('Element is present at index:', res)
