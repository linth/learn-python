# for loop

# example 1: normal list to show every items.
fruits = ['apple', 'banana', 'cherry']

for f in fruits:
    if f == 'banana':
        break
    print(f)

# for x in 'banana':
#     print(x)

# example 2: wuth range() to show data.
for i in range(1, 6): # i = 1 to 5
    print('the value equals to {}'.format(i))

for i in range(6): # i = 0 to 5
    print('the value = {}'.format(i))
else:
    print('the program is finished.')

# example 3: Nested Loops
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print('the pair of word is {0}, {1}'.format(x, y))

# example 4: print index and value of list in for loop.
nums = [2, 7, 11, 15]
for index, val in enumerate(nums):
    print('the index: {0}, the value: {1}'.format(index, val))

# example 5: 9x9 using for "for loop".
# method 1
for i in range(1, 10):
    for j in range(1, 10):
        # print('{0} x {1} = {2}'.format(i, j, i*j))
        pass
# method 2
# j = 1
for i in range(1, 10):
    j = 1
    while j < 10:
        # print('{0} x {1} = {2}'.format(i, j, i*j))
        j += 1

# mtehod 3
