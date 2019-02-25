'''
    basic list.
'''

def ex1():
    # list []
    list1 = ['george', 'mary', 2019, 100]
    list2 = [1, 2, 3, 4, 5]

    print(list1)
    print(list1[0]) # george
    print(list1[1:3]) # ['mary', 2019]
    print(list2)


def ex2():
    # add, update, delete
    list = []
    list.append('google')
    list.append('facebook')

    list1 = ['george', 'mary', 2019, 100]
    del list1[2]
    print(list1) # ['george', 'mary', 100]

def ex3():
    list1 = ['george', 'mary', 2019, 100]
    list2 = [1, 2, 3, 4, 5]
    # len
    len(list1)
    len(list2)
    # return min value
    print(min(list2))
    # return max value
    print(max(list2))
    # count
    print(list2.count(1))
    # insert a obj to the list.
    list1.insert(2, 199)
    print(list1)
    # reverse
    list1.reverse()
    print(list1)
    # sort
    list3 = [8, 2, 11, 7, 10]
    list3.sort()
    print(list3)

if __name__ == '__main__':
    ex1()
    ex2()
    ex3()
