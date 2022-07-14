"""
Lambda function
    - func = lambda 參數1, 參數2, ... : 運算式
    - 三元運算子(ternary conditional operator)

盡量習慣使用簡單的lambda function.


[結論] 比較一下Lambda函式與一般函式(Function)的差異為：
    - Lambda函式不需要定義名稱，而一般函式(Function)需定義名稱。
    - Lambda函式只能有一行運算式，而一般函式(Function)可以有多行運算式。
    - Lambda在每一次運算完會自動回傳結果，而一般函式(Function)如果要回傳結果要加上 return 關鍵字。

    
Reference:
    - https://medium.com/seaniap/python-lambda-%E5%87%BD%E5%BC%8F-7e86a56f1996
    - https://jianjiesun.medium.com/python%E7%AD%86%E8%A8%98-6-%E4%B8%89%E5%85%83%E9%81%8B%E7%AE%97%E5%AD%90-ternary-conditional-operator-72e200575e49
    - https://juejin.cn/post/6988877471500206093
"""

multiply = lambda x, y : x*y

seq_num = lambda x : x ** 2

sum_of_two_num = lambda x, y : x + y

is_adults = lambda age : True if age > 18 else False
is_odd = lambda num : num % 2 != 0

if __name__ == '__main__':
    print(multiply(4, 2)) # 8
    print(seq_num(3)) # 9    
    print(sum_of_two_num(1, 2)) # 3
    
    print(is_adults(11)) # False
    print(is_adults(21)) # True
    
    print(is_odd(3)) # True 
    print(is_odd(4)) # False