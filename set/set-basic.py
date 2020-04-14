# basic concept
# set like dictionary, 不重複、無順序


def example():
    s = {"apple", "banana", "cherry"}
    print('The set = {}'.format(s))
    print("banana" in s) # True


def add_set_example():
    """ Once a set is created, you cannot change its items, but you can add new items. """
    s = {"apple", "banana", "cherry"}
    s.add("orange")
    print('The set = {}'.format(s))
    print('The length of set is {}'.format(len(s)))


def remove_the_set_example():
    s = {"apple", "banana", "cherry"}
    s.remove("banana") # If the item to remove does not exist, remove() will raise an error.
    print('After deleting the banana, the set becomes {}'.format(s)) # {'cherry', 'apple', 'orange'}


def discard_the_set_example():
    s = {"apple", "banana", "cherry"}
    s.discard("banana") # If the item to remove does not exist, discard() will NOT raise an error.
    print('After discarding the banana, the set becomes {}'.format(s)) # {'cherry', 'apple', 'orange'}


def pop_the_set_example():
    s = {"apple", "banana", "cherry"}
    s.pop() # remove the lastest one.
    print('Deleting the lastest one in the set, and the set is {}'.format(s)) # {'apple', 'orange'}


def clear_the_set_example():
    s = set()
    s.add('apple')
    s.add('banana')
    s.add('cherry')
    s.clear() # empties the set
    print('Clearing the set, and the set is {}'.format(s))


def del_the_set_example():
    s = set()
    s.add('apple')
    s.add('banana')
    s.add('cherry')
    del s # delete the set completely
    # print(set) # UnboundLocalError: local variable 'set' referenced before assignment


def example2():
    t3 = set(("apple", "banana", "cherry"))
    print(t3)


def main():
    example()
    example2()

    add_set_example()
    remove_the_set_example()
    discard_the_set_example()
    pop_the_set_example()
    clear_the_set_example()
    del_the_set_example()


if __name__ == '__main__':
    main()
