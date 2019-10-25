import math

'''
References:
    - https://www.geeksforgeeks.org/binary-search/
'''

def binary_search(arr, l, r, x):
    if r >= 1:
        pass
    else:
        # Element is not present in the array
        return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    res = binary_search(arr, 0, len(arr)-1, x)

    if res is not -1:
        print('Element is present at index', res)
    else:
        print("Element is not present in array")
