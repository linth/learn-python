'''
跨 thread 的調度範例:



Reference:
    - https://docs.python.org/zh-tw/3/library/asyncio-task.html#running-in-threads
'''
# import asyncio


# Create a coroutine
# coro = asyncio.sleep(1, result=3)

# Submit the coroutine to a given loop
# future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
# assert future.result(timeout) == 3