'''
非同步阻塞 (synchronous + blocking)
    - 使用 await 方式條列出來，皆會使用順序方式執行完畢。


[思考]: 嘗試 main1, main2 使用裝飾器去計算時間會有問題。


Reference:
    - https://juejin.cn/post/7095400034165850148
'''
import asyncio


async def fn2():
    print("fn2")


async def fn1():
    print("start fn1")
    await fn2()
    print("end fn1")


# 請注意 main1 跟 main2 之間的任務順序
async def main1():
    print("start main")
    await fn2()
    await fn1()
    print("end main")


async def main2():
    print("start main")
    await fn1()
    await fn2()
    print("end main")


if __name__ == '__main__':
    # 非同步函式執行    
    # 請注意 main1 跟 main2 之間的任務順序
    # asyncio.run(main1())    
    asyncio.run(main2())


''' main1()
start main
fn2
start fn1
fn2
end fn1
end main
'''


''' main2()
start main
start fn1
fn2
end fn1
fn2
end main
'''