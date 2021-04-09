"""
datetime, timedelta

Reference:
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017648783851616
"""
from datetime import datetime
from datetime import timedelta


def increase_time(d: int = 0, h: int = 0, m: int = 0, sec: int = 0):
    now = datetime.now()
    print(f'now time:       {now}')
    print(f'increased time: {now + timedelta(days=d, hours=h, minutes=m, seconds=sec)}')


if __name__ == '__main__':
    # 現在時間
    now = datetime.now()
    print(f'now date and time: {now}') # example: 2021-04-09 22:50:31.616756

    certain_time = datetime(1999, 1, 1, 12, 32, 6)
    print(f'Time: {certain_time}') # 1999-01-01 12:32:06

    # datetime convert to timestamp.
    d2t = certain_time.timestamp()
    print(f'the timestamp: {d2t} sec')

    # timestamp convert to datetime.
    # (當地時間)
    t2d = datetime.fromtimestamp(d2t)
    print(f'the datetime: {t2d}')

    # (UTC時間)
    utc_t2d = datetime.utcfromtimestamp(d2t)
    print(f'the UTC time: {utc_t2d}')

    # datetime 轉換成 string
    s = now.strftime('%a, %b %d, %H:%M:%S')
    print(f'Now: {s}')

    # string 轉換成 datetime
    r = datetime.strptime('2020-10-22 14:22:7', '%Y-%m-%d %H:%M:%S')
    print(f'Time: {r}')

    increase_time(1, 1, 9)
