'''
Lists and loops
Reference: http://openbookproject.net/thinkcs/python/english3e/lists.html
'''

def example1():
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

    # for i in friends:
    #     print('{}'.format(i))
    #
    # for i in range(len(friends)):
    #     print(friends[i])

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
    # number [for number in range(20)]
    pass


def main():
    example1()
    # example2()
    # example3()


if __name__ == '__main__':
    main()
