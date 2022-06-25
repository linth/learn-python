'''
aiohttp example
    - Python 的 aiohttp 套件提供了非同步版本的 HTTP 協定相關功能。以下是 aiohttp 的基本使用範例：


設計架構應該可以使用
    - 一堆 task functions
    - 一堆 task流程 [順序程式碼] 或 [併發程式碼]?


Reference:
    - https://officeguide.cc/python-asyncio-aiohttp-asynchronous-io-tutorial-examples/
'''
# from time import time
# from unittest import result
# import aiohttp
# import asyncio


# def do_requests(session):
#     return session.get('https://pokeapi.co/api/v2/pokemon/151')


# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = []
        
#         # 指定網站網址
#         # pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
#         for _ in range(0, 10):
#             tasks.append(do_requests(session))
            
#         result = await asyncio.gather(*tasks)
        
#         for r in result:
#             print('url: ', r.status)


# if __name__ == '__main__':
#     s = time()
#     asyncio.run(main())
#     e = time()
#     print('total time:', e-s)

