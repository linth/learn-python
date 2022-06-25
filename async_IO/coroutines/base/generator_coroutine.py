'''
使用生成器來支援非同步程式設計

協程 (coroutine) 的想法是有一個 function，執行時可以暫停 (suspend)，稍後再恢復執行。
此部分是採用生成器來當作協程 (coroutine) 來運作，支援非同步程式設計。

Reference:
    - 
'''

def stream_db_record(handler):
    try:
        while True:
            yield handler.read_n_data_record(10)
    except GeneratorExit:
        handler.close()

print(stream_db_record([1, 2, 3, 4, 5, 6]))