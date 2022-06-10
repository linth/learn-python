
# 可等待 object
如果一個 object 可以在 await 語句中使用，那麼它就是可等待 object。許多 asyncio API 都被設計為接受可等待 object。

可等待 object 有三種主要類型: 
    - 協程 (coroutine), 
    - 任務 
    - Future
