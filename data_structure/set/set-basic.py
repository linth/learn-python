# basic concept
# set like dictionary, 不重複、無順序


def example():
    s = {"apple", "banana", "cherry"}
    print('The set = {}'.format(s))
    print("banana" in s) # True


def example2():
    t3 = set(("apple", "banana", "cherry"))
    print(t3)


def add_item():
    """
    add function.
    Once a set is created, you cannot change its items, but you can add new items.
    :return:
    """
    s = {"apple", "banana", "cherry"}
    s.add("orange")
    print(f'The set = {s}')
    print(f'The length of set is {s}')


def remove_item():
    """
    remove function.
    :return:
    """
    s = {"apple", "banana", "cherry"}
    s.remove("banana") # If the item to remove does not exist, remove() will raise an error.
    print(f'After deleting the banana, the set becomes {s}') # {'cherry', 'apple'}


def discard_item():
    """
    discard function.
    :return:
    """
    s = {"apple", "banana", "cherry"}
    s.discard("banana") # If the item to remove does not exist, discard() will NOT raise an error.
    print(f'After discarding the banana, the set becomes {s}') # {'cherry', 'apple'}


def pop_item():
    """
    pop function.
    :return:
    """
    s = {"apple", "banana", "cherry"}
    s.pop() # remove the lastest one.
    print(f'Deleting the lastest one in the set, and the set is {s}') # {'apple', 'orange'}


def clear_item():
    """
    clear function.
    :return:
    """
    s = set()
    s.add('apple')
    s.add('banana')
    s.add('cherry')
    s.clear() # empties the set
    print(f'Clearing the set, and the set is {s}')


def del_item():
    """
    delete function.
    :return:
    """
    s = set()
    s.add('apple')
    s.add('banana')
    s.add('cherry')
    del s # delete the set completely
    # print(set) # UnboundLocalError: local variable 'set' referenced before assignment


def main():
    example()
    example2()

    add_item()
    remove_item()
    discard_item()
    pop_item()
    clear_item()
    del_item()


if __name__ == '__main__':
    main()
