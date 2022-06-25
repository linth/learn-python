
# 可等待 object
如果一個 object 可以在 await 語句中使用，那麼它就是可等待 object。許多 asyncio API 都被設計為接受可等待 object。

可等待 object 有三種主要類型: 
    - 協程 (coroutine), 
    - 任務 
    - Future

---

## [A quick refresher on stacks and frames](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-1.html)
在文章內，有詳細說明 call function 並 stack 依序進行順序。
有效了解每個步驟的流程跟運作，值得參考。


## Reference:
    - https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-1.html