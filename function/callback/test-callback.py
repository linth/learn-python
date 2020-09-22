

def is_even(value):
    return value % 2 == 0


def get_new_list(num: list, callback) -> dict:
    d = dict()
    even_list, odd_list = [], []

    for i in num:
        res = callback(i)
        if res is True:
            even_list.append(i)
        else:
            odd_list.append(i)
    d['even_list'] = even_list
    d['odd_list'] = odd_list
    return d


class A:
    pass


if __name__ == '__main__':
    l = [2, 3, 4, 6, 7, 11, 13]
    res_d = get_new_list(l, is_even)
    print(res_d)
