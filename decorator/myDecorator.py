

def myDeco(callback):

    def run():
        print(f'裝飾器程式碼...')
        callback()
    return run


@myDeco
def test():
    print(f'test()程式碼...')


test()
