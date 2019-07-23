'''
    basic list.
    Reference: http://openbookproject.net/thinkcs/python/english3e/lists.html
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
    print('The min of list2 is {}'.format(min(list2)))
    # return max value
    print('The max of list2 is {}'.format(max(list2)))
    # count
    print('In the list2, there are {} for number 1.'.format(list2.count(1)))
    print('In the list2, there are {} number'.format(len(list2)))
    # insert a obj to the list.
    list1.insert(2, 199)
    print('list1 = {}'.format(list1))
    # reverse
    list1.reverse()
    print('The reverse list1 equals to {}'.format(list1))
    # sort
    list3 = [8, 2, 11, 7, 10]
    print('before sorting = {}'.format(list3))
    list3.sort()
    print('after sorting = {}'.format(list3))

def ex4():
    a = ['A', 'B', 'C', 'D', 'E', 'F']
    b = ['2', '3', '10']
    for i in range(len(a)):
        print(a[i])

    # list operations
    c = a + b
    print('a + b = {}'.format(c))
    print('c = {}'.format(c*2))

    # slices
    print(c[1:5])
    print(c[4:])
    print(c[:])

    # mutable
    c[0] = 'george'
    c[3] = 'peter'
    print(c)

    # deletion: the del statement removes an element from a list
    d = ['george', 'B', 'C', 'peter', 'E', 'F', '2', '3', '10']
    print('before delete the d = {}'.format(d))
    del d[3:]
    print('after delete the d = {}'.format(d))

def ex5():

    a, b = 'banana', 'banana'
    print('a is b = {}'.format(a is b)) # a is b = True
    c, d = 1, 1
    print('c is d = {}'.format(c is d)) # c is d = True
    # Objects and references
    # e and f have the same value but do not refer to the same object.
    e, f = [1, 2, 3], [1, 2, 3]
    print('e is f = {}'.format(e is f)) # e is f = False
    # Aliasing
    e = f
    print('e is f = {}'.format(e is f)) # e is f = True
    e[0] = 5
    print('f = {}'.format(f)) # f = [5, 2, 3]

    # cloning list.
    g = [4, 5, 6]
    h = g[:]
    print('g is h = {}'.format(g is h)) # g is h = False

if __name__ == '__main__':
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
