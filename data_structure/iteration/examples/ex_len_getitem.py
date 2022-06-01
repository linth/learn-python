'''
迭代 (iteration) 
    - 是透過自己的協定 (iterator 協定)，在python運作的。
    - 當你使用 `for i in object: ...` 去迭代一個物件時候，python做了兩件事情：
        * 檢查有沒有包含兩種迭代器方法: __next__ 和 __iter__
        * 檢查物件是不是序列，且具有 __len__ 和 __getitem__

'''
from datetime import timedelta
from datetime import date


class DateRangeSequence:
    
    def __init__(self, start_date, end_date): 
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()
        
    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days
    
    def __getitem__(self, day_no):
        return self._range[day_no]
    
    def __len__(self):
        return len(self._range)
    
if __name__ == '__main__':
    dr = DateRangeSequence(
        date(2022, 5, 20),
        date(2022, 6, 3)
    )
    
    for day in dr:
        print(day)
    
    