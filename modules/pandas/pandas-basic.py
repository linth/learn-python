import pandas as pd

'''
References:
    - https://medium.com/@weilihmen/python-pandas-%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C%E6%95%99%E5%AD%B8-%E6%88%90%E7%B8%BE%E8%A1%A8-f6d0ec4f89
'''

scores = pd.Series({
    'george': 100,
    'may': 98,
    'john': 78,
    'peter': 85,
})


def add_a_new_data():
    scores['haha'] = 55


def cal_average_standard():
    return scores.describe()


def cal_mean():
    return scores.mean()


def use_list_as_index():
    c = ['apple','banana','cat','dog'] # array 1.
    d = [123,456,789,56789] # array2.

    res = pd.Series(d, index=c)
    print(res)
    return res


def use_date_as_index():
    f = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = pd.Series(f, pd.date_range(start='2019-10-29', end='2019-11-6'))
    print(res)
    return res


def detect_the_value():
    print(scores > 84)
    print((scores > 60) & (scores < 96))


def cal_scores():
    new_score = scores**0.5 * 10
    print('The new score equals to {}'.format(new_score))
    return new_score


def create_dataframe():
    # array + dict
    student = [
        {'name': 'george', 'math': 90, 'chinese': 80},
        {'name': 'may', 'math': 78, 'chinese': 50},
        {'name': 'haha', 'math': 55, 'chinese': 30}
    ]
    student_df = pd.DataFrame(student)
    print('student_df', student_df)

    # pure dict by using from_dict
    student2 = {
        'name': ['george', 'may', 'haha'],
        'chinese': [80, 50, 30],
        'math': [90, 78, 55],
    }
    student2_df = pd.DataFrame.from_dict(student2)
    print('student2_df', student2_df)


if __name__ == '__main__':
    # print(scores)
    add_a_new_data()
    # print(scores)

    # print('The total information is for scores: ', cal_average_standard())
    # print('The mean of scores', cal_mean())

    # use_list_as_index()
    use_date_as_index()
    detect_the_value()
    cal_scores()
    create_dataframe()
