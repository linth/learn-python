from datetime import datetime
from datetime import timedelta
from datetime import timezone


if __name__ == '__main__':
    now_utc = datetime.utcnow()
    now = datetime.now()
    print(f'now:     {now}, {type(now)}, {now.tzinfo}')
    print(f'now_utc: {now_utc}, {type(now_utc)}, {now_utc.tzinfo}')

    d1 = datetime(2020, 12, 30, 11, 3, 50, tzinfo=timezone.utc)
    print(f'd1:      {d1}, {d1.tzinfo}')
    d = datetime(2022, 1, 3)
    print(d, d.year, d.month, d.day, d.isocalendar()[1])


