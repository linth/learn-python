'''
銀行帳號範例:
    - 使用 100 threads 對同一個銀行帳戶轉帳，在沒保護的情狀下，我們有可能會得到錯誤結果。
    

臨界區段（Critical section）指的是一個存取共用資源（例如：共用裝置或是共用記憶體）的程式片段，而這些共用資源有無法同時被多個執行緒存取的特性。
    - Synchronization 同步問題

Reference:
    - https://mropengate.blogspot.com/2015/01/operating-system-ch6-synchronization.html
    - https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/13.%E8%BF%9B%E7%A8%8B%E5%92%8C%E7%BA%BF%E7%A8%8B.md
'''
from time import sleep
from threading import Thread


class Account(object):    
    def __init__(self):
        self._balance = 0
        
    def deposit(self, money):
        # 計算存款後的餘額
        new_balance = self._balance + money
        
        # 模擬存款業務需要 0.01 秒時間
        sleep(0.01)
        
        # 修改帳戶餘額
        self._balance = new_balance
        
    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
        
    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    
    # 建立 100 個存款 thread 向某帳號存錢
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
        
    # 等待所有存款的 thread 都執行完畢
    for t in threads:
        t.join()
        
    print('how much memory:', account.balance)


if __name__ == '__main__':
    main() # 遠遠低於 100
    


