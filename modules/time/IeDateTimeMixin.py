"""
Reference
    -

Keyword:
    - strftime: convert to string from datetime (format the format of time).
    - strptime: convert to datetime format from string.
"""
import time
import datetime


class IeDateTimeMixin:
    """ the common calculation of datetime and usually used function for datetime. """
    @staticmethod
    def get_today() -> datetime:
        return datetime.datetime.today()

    def get_yesterday(self):
        """
        get datetime yesterday.
        :return:
        """
        return self.get_today() - datetime.timedelta(days=1)

    def get_a_week_ago(self) -> datetime:
        """
        get datetime before 7 days.
        :return:
        """
        return self.get_today() - datetime.timedelta(days=7)

    def get_8hr_age(self) -> datetime:
        """
        get datetime before 8 hr age.
        :return:
        """
        return self.get_today() - datetime.timedelta(hours=8)

    @staticmethod
    def diff(start: datetime, end: datetime) -> datetime:
        """
        the diff between two days.
        :return:
        """
        return start - end

    @staticmethod
    def datetime_to_str(dt: datetime, format_dt: str = '%Y-%m-%d %H:%M:%S') -> str:
        """
        convert to string from datetime.
        :return:
        """
        return datetime.datetime.strftime(dt, format_dt)

    @staticmethod
    def str_to_datetime(str_dt: str, format_dt: str = '%Y-%m-%d %H:%M:%S') -> datetime:
        """
        convert to datetime from string.
        :return:
        """
        return datetime.datetime.strptime(str_dt, format_dt)
