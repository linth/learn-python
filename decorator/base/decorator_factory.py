"""
裝飾器工廠的基本寫法

如果使用裝飾器工廠，則裝飾器需要 ＠myFactory()
"""

def myFactory(base):
    def myDeco(callback):
        def run():
            print(f'裝飾器內的程式 ', base)
            result = base * 2
            callback(result)
        return run
    return myDeco


@myFactory(10)
def test(result):
    print(f'general function...', result)


test()

# 裝飾器內的程式  10
# general function... 20