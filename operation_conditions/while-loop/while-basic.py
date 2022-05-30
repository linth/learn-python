# while loop

# example 1: check the number is less than 6 or not.
i = 1
while i < 6:
    print('the value of i equals to {}'.format(i))
    i += 1
else:
    print('the value of i is larger than 6.')

# example 2: check the number is less than 3 and close/continue the program with break/continue
j = 1
while j < 6:
    print('the value of j equals to {}'.format(j))
    if j == 3:
        break
        # continue
    j += 1

# example 3: classify the even and odd of list.
nums = [12, 37, 5, 42, 8, 3]
even = []
odd = []
print('the array of nums: {}'.format(nums))

while len(nums) > 0:
    num = nums.pop()
    if num % 2 == 0:
        even.append(num) # even
    else:
        odd.append(num) # odd
print('the even of nums is {}'.format(even))
print('the odd of nums is {}'.format(odd))

# example 4: 9X9 using while loop.
k = 1
l = 1
while k < 10:
    while l < 10:
        print('{} x {} = {}'.format(k, l, k*l))
        l += 1
    l = 1
    k += 1

# example 5: 
