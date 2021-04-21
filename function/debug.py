"""
pycharm debug method.
- step over (F8): 單步執行，遇子函數不進入單步執行，而是執行子函數完再停止。
- step into (F7): 單步執行，遇子函數進入，且單步執行，有時候會跳到原始碼去執行。
- step into my code (alt + shift + F7): 單步執行，遇子函數進入，且單步執行，不會跳到原始碼去執行。
- step out (shift + F8): 已經進入某個函數中，不想繼續看了，跳出當前的函數，返回呼叫此函數的地方。
- resume program (F9): 繼續恢復執行程式，到下個斷點處。

一般正常操作:
1. 設定好斷點，debug執行
2. F8單步執行
3. 遇到想進去的函數 F7進去
4. 想從函數出來在 shift + F8，跳過不想看的地方。
5. F9 直接到下個斷點

Reference:
    - https://zhuanlan.zhihu.com/p/62610785
"""


def sum_demo(x, y):
    for _ in range(2):
        x += 1
        y += 1
        result = x + y
    return result


if __name__ == '__main__':
    res = sum_demo(1, 1)
    print(f'res: {res}')
