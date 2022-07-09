'''
生成器產生偶數
    - 動態產生可疊代的資料，搭配 for 迴圈使用。
    - 使用 yield 語法，呼叫時回傳生成器。 

Reference:
    - https://www.youtube.com/watch?v=x6MNOSRY5EM&t=4s
'''
def generate_even(max):
    number = 0
    while number < max:
        yield number
        number += 2


evenGenerator = generate_even(20)

for data in evenGenerator:
    print(data) # 0, 2, 4, 6, 8, 10, 12, 14, 16, 18