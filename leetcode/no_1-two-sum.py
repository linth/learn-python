"""
No. 1 two sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

reference:
    - https://leetcode.com/problems/two-sum/
    - https://blog.techbridge.cc/2019/08/30/leetcode-pattern-two-pointer/
"""


def first_time(*args):
    # Time complexity is O(n^2)
    # Space complexity is O(1)
    print('args = {}, the type of args = {}'.format(args, type(args))) # args = ({'nums': [2, 7, 11, 15], 'target': 9},), the type of args = <class 'tuple'>
    print('args[\'nums\'] = {}, and the type of args[\'nums\'] = {}'.format(args[0]['nums'], type(args[0]['nums']))) # args['nums'] = [2, 7, 11, 15], and the type of args['nums'] = <class 'list'>

    # k = args[0]['nums'][0]
    for i in range(0, len(args[0]['nums'])):
        # print('i', i)
        for index, value in enumerate(args[0]['nums']):
            if index == i or index < i:
                pass
            else:
                # print(index, value)
                if value + args[0]['nums'][i] == args[0]['target']:
                    # print([i, index])
                    return [i, index]


class Solution:
    def online1(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target-nums[i]], i]

    def online2(self, nums, target):
        d ={}
        for index, value in enumerate(nums):
            n = target - value
            if n not in d:
                d[nums] = index
            else:
                return [d[n], index]


def two_sum(*args):
    print('args = {}, the type of args = {}'.format(args, type(args)))


def two_sum2(**kwargs):
    print('kwargs = {}, the type of kwargs = {}'.format(kwargs, type(kwargs)))


def main():
    d = {'nums': [2, 7, 11, 15], 'target': 9}
    nums, target = [2, 7, 11, 15], 9
    # res = first_time(d)    # using args as parameters.
    s = Solution()
    res = s.online1(nums, target)
    # two_sum2(nums=[2, 7, 11, 15], target=9) # using kwargs as parameters.

    print('The res is {}, and the type of res is {}'.format(res, type(res)))


if __name__ == '__main__':
    main()
