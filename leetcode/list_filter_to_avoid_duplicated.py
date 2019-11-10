

# example 1: array
def list_filter_to_avoid_duplicated(arr):
    new_arr = []
    flag = False

    for i in arr:
        for j in new_arr:
            if i == j:
                flag = True

        if flag is False:
            new_arr.append(i)
    return new_arr


# example 2: using class to structure them.
class ListAvoidDuplicate:
    def list_filter_to_avoid_duplicated(self, arr):
        new_arr = []

        for i in arr:
            flag = False
            for j in new_arr:
                if i == j:
                    flag = True

            if flag is False:
                new_arr.append(i)
        return new_arr


# using inheritance  to design 3-tier.
class ListAvoidDuplicateBased:
    def decide(self):
        pass

    def list_filter_to_avoid_duplicated(self):
        pass


class ListAvoidDuplicateProcess(ListAvoidDuplicateBased):
    def list_filter_to_avoid_duplicated(self, *args):
        pass


class ListAvoidDuplicateImplement(ListAvoidDuplicateProcess):
    def decide(self, *args, **kwargs):
        res = []

        if args and kwargs:
            print('There are both, args = {}; kwargs = {}'.format(args, kwargs))
        elif args and not kwargs:
            print('There is args = ', args)
            if len(args) == 1 and isinstance(args[0], list):
                res = self.list_filter_to_avoid_duplicated(args[0])
            else:
                print('Please re-type the argument.')
        elif not args and kwargs:
            print('There is kwargs = ', kwargs)
        else:
            pass
        return res

    def list_filter_to_avoid_duplicated(self, *args):
        new_arr = []

        for i in args[0]:
            flag = False
            for j in new_arr:
                if i == j:
                    flag = True

            if flag is False:
                new_arr.append(i)
        return new_arr


if __name__ == '__main__':
    # example 1.
    arr = [1, 2, 6, 3, 2, 6, 2, 8]
    # print('arr = ', arr)
    # res = list_filter_to_avoid_duplicated(arr)
    # print('res = ', res)

    #  example 2.
    l = ListAvoidDuplicate()
    # res = list_filter_to_avoid_duplicated(arr)
    # print(res)

    # res2 = l.list_filter_to_avoid_duplicated(arr, name='george')
    res2 = l.list_filter_to_avoid_duplicated(arr)
    print('res2', res2)

    #  example 3.
    res3 = ListAvoidDuplicateImplement().decide(arr)
    print('res3', res3)
