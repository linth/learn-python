'''
迭代 (iteration) 
    - 是透過自己的協定 (iterator 協定)，在python運作的。
    - 當你使用 `for i in object: ...` 去迭代一個物件時候，python做了兩件事情：
        * 檢查有沒有包含兩種迭代器方法: __next__ 和 __iter__
        * 檢查物件是不是序列，且具有 __len__ 和 __getitem__

'''
from datetime import timedelta
from datetime import date


class DateRangeIterable:
    
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date
        
    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration()
        
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today
    
    
if __name__ == '__main__':
    dr = DateRangeIterable(
        date(2022, 5, 28),
        date(2022, 6, 3)
    )
    
    for day in dr:
        print(day)
    
