'''
Reference:
    - https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/369869/
'''
import datetime
import time
import calendar


def get_today_date():
    # get today date bt using two methods.
    # method 1.
    today = datetime.datetime.now()
    # method 2.
    today1 = datetime.date.today()
    return today # or today1.


def get_yesterday_date():
    today = get_today_date()
    yesterday = today - datetime.timedelta(days=1)
    print('The date of yesterdat = {}.'.format(yesterday)) # The date of yesterdat = 2019-08-02 22:04:31.164018.
    return yesterday


def str_to_datetime(str, format):
    return datetime.datetime.strptime(str, format)


def example1():
    local_date = time.localtime()
    print('The time of local is "{}" by using the time.localtime function.'.format(local_date)) # The time of local is "time.struct_time(tm_year=2019, tm_mon=8, tm_mday=3, tm_hour=22, tm_min=4, tm_sec=31, tm_wday=5, tm_yday=215, tm_isdst=0)" by using the time.localtime function.


def example2():
    # the string converts to time date.
    str_date = '2019-08-02'
    res = str_to_datetime(str_date, "%Y-%m-%d")
    print('The string of "{}" converts to the datetime: "{}", and the type of datetime is {}'.format(str_date, res, type(res))) # The string of "2019-08-02" converts to the datetime: "2019-08-02 00:00:00", and the type of datetime is <class 'datetime.datetime'>


def main():
    # example1()
    # get_yesterday_date()
    # print(str_to_datetime('%Y-%m-%d', time.localtime()))
    example2()

if __name__ == '__main__':
    main()


