'''
Lists and loops
Reference: http://openbookproject.net/thinkcs/python/english3e/lists.html
'''

def example1():
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

    for i in friends:
        print('{}'.format(i))

    for i in range(len(friends)):
        print(friends[i])

    for i in enumerate(friends):
        print('{}'.format(i)) # (0, 'Joe') (1, 'Zoe') (2, 'Brad') (3, 'Angelina') (4, 'Zuki') (5, 'Thandi') (6, 'Paris')
        print('{} - {}'.format(i[0], i[1]))

    for (index, value) in enumerate(friends):
        friends[index] = value * 2
    print('{}'.format(friends)) # ['JoeJoe', 'ZoeZoe', 'BradBrad', 'AngelinaAngelina', 'ZukiZuki', 'ThandiThandi', 'ParisParis']

def example2():
    for number in range(20):
        if number % 3 == 0:
            print('{}'.format(number))

def example3():
    list = [5, 27, 3, 11]

    # append method.
    list.append(5)
    print('list = {}'.format(list)) # list = [5, 27, 3, 11, 5]

    # insert [index, value]
    list.insert(1, 11)
    print('After inserting the list = {}'.format(list)) # After inserting the list = [5, 11, 27, 3, 11]

    #  calculate the number of what you want to know the number.
    num_of_number = list.count(11)
    print('How many times is 11 in the list? Answer: {}'.format(num_of_number)) # How many times is 11 in the list? Answer: 2

    # put the whole list into end of list.
    list.extend([1, 2, 3, 4])
    print('The list extends to {}'.format(list)) # The list extends to [5, 11, 27, 3, 11, 1, 2, 3, 4]

    # find index of first 27 in the list.
    res = list.index(27)
    print('The index of the first 27 in the list: {}'.format(res)) # The index of the first 27 in the list: 2

    # reverse the list.
    list.reverse()
    print('The list is reversed = {}'.format(list)) # The list is reversed = [4, 3, 2, 1, 11, 3, 27, 11, 5]

    # sort the list.
    list.sort()
    print(('The list is sorting to {}'.format(list))) # The list is sorting to [1, 2, 3, 3, 4, 5, 11, 11, 27]

    # remove the first value of list.
    list.remove(11)
    print('The first 11 is removed to {}'.format(list)) # The first 11 is removed to [1, 2, 3, 3, 4, 5, 11, 27]


def main():
    example1()
    example2()
    example3()


if __name__ == '__main__':
    main()
