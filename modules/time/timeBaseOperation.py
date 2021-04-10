"""
datetime, timedelta

最好的模式就是全部 time 轉換成 timestamp

Reference:
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017648783851616
"""
from datetime import datetime
from datetime import timedelta


def cal_time(d: int = 0, h: int = 0, m: int = 0, sec: int = 0):
    """
    example: calculate datetime by using timedelta.
    :param d:
    :param h:
    :param m:
    :param sec:
    :return:
    """
    now = datetime.now()
    print(f'now time:       {now}')
    print(f'increased time: {now + timedelta(days=d, hours=h, minutes=m, seconds=sec)}')
    return now + timedelta(days=d, hours=h, minutes=m, seconds=sec)


if __name__ == '__main__':
    # 現在時間
    now = datetime.now()
    utc_now_time = datetime.utcnow()
    print(f'now date and time: {now}') # example: 2021-04-10 09:58:11.003160
    print(f'utc now date and time: {utc_now_time}') # example: 2021-04-10 01:58:11.003160

    certain_time = datetime(1999, 1, 1, 12, 32, 6)
    print(f'Time: {certain_time}') # 1999-01-01 12:32:06

    # datetime => timestamp.
    d2t = certain_time.timestamp()
    print(f'the timestamp: {d2t} sec')

    # timestamp => datetime.
    # (當地時間)
    t2d = datetime.fromtimestamp(d2t)
    print(f'Local time: {t2d}')

    # (UTC時間)
    utc_t2d = datetime.utcfromtimestamp(d2t)
    print(f'UTC time: {utc_t2d}')

    # datetime 轉換成 string
    s = now.strftime('%a, %b %d, %H:%M:%S')
    print(f'Now: {s}')

    # string 轉換成 datetime
    r = datetime.strptime('2020-10-22 14:22:7', '%Y-%m-%d %H:%M:%S')
    print(f'Time: {r}')

    cal_time(1, 1, 9)

