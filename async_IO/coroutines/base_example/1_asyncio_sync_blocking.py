'''
同步阻塞 (synchronous + blocking)
    - 執行時候會按照順序依序完成後，才會接續下一個任務。

'''
import time


# 同步函式
def funOne():
    time.sleep(1)
    return ("function one.")


def funTwo():
    time.sleep(1)
    return ("function two.")


def funThree():
    time.sleep(1)
    return ("function three.")


def run():
    print(funOne())
    print(funTwo())
    print(funThree())



if __name__ == '__main__':    
    # 同步函式執行
    run()
    