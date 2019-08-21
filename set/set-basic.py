# basic concept
# set like dictionary, 不重複、無順序

def example():
    set = {"apple", "banana", "cherry"}
    print('The set = {}'.format(set))
    print("banana" in set) # True


'''
    Once a set is created, you cannot change its items, but you can add new items.
'''
def add_set_example():
    set = {"apple", "banana", "cherry"}
    set.add("orange")
    print('The set = {}'.format(set))
    print('The length of set is {}'.format(len(set)))

def remove_the_set_example():
    set = {"apple", "banana", "cherry"}
    set.remove("banana") # If the item to remove does not exist, remove() will raise an error.
    print('After deleting the banana, the set becomes {}'.format(set)) # {'cherry', 'apple', 'orange'}

def discard_the_set_example():
    set = {"apple", "banana", "cherry"}
    set.discard("banana") # If the item to remove does not exist, discard() will NOT raise an error.
    print('After discarding the banana, the set becomes {}'.format(set)) # {'cherry', 'apple', 'orange'}

def pop_the_set_example():
    set = {"apple", "banana", "cherry"}
    set.pop() # remove the lastest one.
    print('Deleting the lastest one in the set, and the set is {}'.format(set)) # {'apple', 'orange'}

def clear_the_set_example():
    set.clear() # empties the set
    print('Clearing the set, and the set is {}'.format(set))

def del_the_set_example():
    del set # delete the set completely
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
