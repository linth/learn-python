'''
生成器 generator
    - 動態產生可疊代的資料，搭配 for 迴圈使用。
    - 使用 yield 語法，呼叫時回傳生成器。

def function_name():
    yield data
  

Reference:
    - https://www.youtube.com/watch?v=x6MNOSRY5EM&t=4s
'''

def test():
    yield 3
    yield 5


gen = test()

for data in gen:
    print(data) # 3

