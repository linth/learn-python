"""
Reference:
    - https://medium.com/@python.learning/14-hidden-python-features-for-beginners-part-1-77596c614772
"""
from string import ascii_lowercase


def merge_dict(**kwargs):
    """ combine several dictionaries together. """
    return dict(kwargs)


def join_string():
    arr = ["Hello", "everyone.", "My", "name", "is", "George."]
    new_string = " ".join(arr)
    print(f"new_string = \"{new_string}\"")


def find_max_occurrence_from_a_list(arr):
    """ Max occurrence of an item from a list. """
    return max(set(arr), key=arr.count)


def values_swapping(a, b):
    fist, second = a, b
    return (second, fist)


def range_into_list(arr_first, arr_last):
    """ Range into list. """
    return list(range(arr_first, arr_last))


def square_list(arr_first, arr_last):
    return [i**2 for i in range(arr_first, arr_last)]


def dict_comprehension():
    res = {f"item {i}": j for i, j in enumerate(ascii_lowercase) if i < 6}
    print(res)


def add_lists(lst1: list, lst2: list):
    return lst1 + lst2


def add_list_as_index(lst1: list, lst2: list):
    lst1.append(lst2)
    return lst1


def extraction_of_nested_list(lst: list):
    return sum(lst, [])


def unique_items_list(lst: list):
    return list(set(lst))


def list_extend(lst1, lst2):
    lst1.extend(lst2)
    return lst1


if __name__ == '__main__':
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    merge_dict = merge_dict(**d1, **d2)
    print(f"merge_dict = {merge_dict}")

    new_merge_dict = dict(**d1, **d2)
    # new_merge_dict = dict(d1, **d2) # the same as above row.
    print(f"new merge_dict = {new_merge_dict}")

    join_string()

    arr = [1, 2, 2, 4, 2, 2, 3, 1, 5, 4, 4]
    max_value = find_max_occurrence_from_a_list(arr)
    print(f"max_value = {max_value}")

    a, b = 2, 5
    vs_result = values_swapping(a, b)
    print(f"vs_result = {vs_result}")

    range_arr = range_into_list(1, 11)
    print(f"arr = {range_arr}")

    square_list = square_list(1, 11)
    print(f"square list = {square_list}")

    dict_comprehension()

    arr2 = [88, 2]
    add_lists = add_lists(arr, arr2)
    print(f"add_list = {add_lists}")

    add_list_as_index = add_list_as_index(arr, arr2)
    print(f"add_list_as_index = {add_list_as_index}")

    List1 = [[1], [2], [3], [4], [5]]
    extraction_of_nested_list = extraction_of_nested_list(List1)
    print(f"extraction_of_nested_list = {extraction_of_nested_list}")

    unique_items_list = unique_items_list(add_lists)
    print(f"unique_items_list = {unique_items_list}")

    lst1, lst2 = [1, 2], [3, 4]
    list_extend = list_extend(lst1, lst2)
    print(f"list_extend = {list_extend}")

    # print’s end arguments
    lst3 = [1, 1, 1, 2, 3, 4, 5, 1, 2, 3, 1, 5]
    for i in lst3:
        print(i, end="=>")

    # print’s sep argument
    print("\nHello", "world", "and", "everyone", sep="--")
