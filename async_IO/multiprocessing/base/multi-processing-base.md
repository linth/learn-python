# 使用 multi-processing 的差異

## 範例1: 沒使用 multi-processing 
```
請參考 1_not_use_multi-processing.py 範例檔案
```

## 範例2: 有使用 multi-processing
```
請參考 2_use_multi-processing.py 範例檔案
```

## 結論:
    - 無使用 multi-processing 會按順序一點一點執行，執行兩個不相關任務時，需要先等待一個任務完成才會繼續。
    - 使用 multi-processing 可同時啟動任務，並大幅度縮短執行時間。
    - 缺點: 每個任務建立 process 資源會比較大。且適合任務間不需要共享資源的情境。
---

# 使用 multi-thread 的差異

根據上述問題， multi-processing 確實有效改善執行時間效率問題，但是某些任務可能會分享一些資訊給多個任務間進行溝通就可能需要使用 multi-processing 的 Queue class 進行資料共享。
```
請參考 3_two_process_with_counter.py
```

這時候， thread module 也可以實現上述任務，且分享共用資源。

## 直接使用 Thread() 方式來執行
```
請參考 4_use_thread_func.py
```

## 使用繼承 Thread class 方式來執行
```
請參考 5_use_thread_class.py
```

## 結論:
    - 提供 class-based, function-based 寫法
    - 資源占用較小
    - 當使用 thread 時候，就需要考量資源被多個 thread 佔用時，產生的 critical section 問題。

---

[問題] 為什麼當使用 threading 時候，會需要考慮到 critical section?

臨界區段（Critical section）指的是一個存取共用資源（例如：共用裝置或是共用記憶體）的程式片段，而這些共用資源有無法同時被多個執行緒存取的特性。
    - Synchronization 同步問題

## 沒考慮 Critical section 範例
```
請參考 6_not_consider_critical_section.py
```

## 有考慮 Critical section 範例
```
請參考 7_consider_critical_section.py
```

