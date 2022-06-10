'''
Shielding From Cancellation:
    - 用來取消 concurrency 中的 task。

[注意]
! Changed in version 3.10: Removed the loop parameter.
! Deprecated since version 3.10: Deprecation warning is emitted if aw is not Future-like object and there is no running event loop.

Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html
'''
import asyncio


# async def something():
#     print('show something.')


# async def sum():
#     try:
#         res = asyncio.shield(something())
#     except CancelledError:
#         res = None
        
# asyncio.run(sum())
        