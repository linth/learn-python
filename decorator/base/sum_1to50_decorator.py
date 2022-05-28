"""
calculator 1+2+3+... +50

"""

def calculator(callback):
    def cal_sum_one_to_fifty():
        sum = 0
        for i in range(51):
            sum += i
        print('sum', sum)
        callback(sum)
    return cal_sum_one_to_fifty

@calculator
def show_result(sum_of_value):
    print('結果: ', sum_of_value)


@calculator
def show_result_in_english(sum_of_value):
    print('result is ', sum_of_value)


show_result()
show_result_in_english()


"""
裝飾器工廠：
    - 為了讓裝飾器更彈性，可以使用decorator factory.

提供使用者可以自行定義要計算最大值為多少？

"""
def decorator_factory(max):
    def calculator(callback):
        def cal_sum_one_to_fifty():
            sum = 0
            for i in range(max+1):
                sum += i
            callback(sum)
        return cal_sum_one_to_fifty
    return calculator

@decorator_factory(100)
def show_custom_result(sum):
    print(f'sum of value: ', sum)

@decorator_factory(200)
def show_custom_result_in_english(sum):
    print(f'sum of value in english: ', sum)

show_custom_result()
show_custom_result_in_english()