from abc import abstractmethod, ABC
import csv


class BaseData(ABC):
    """ this class is interface class. """
    pass


class FileData(BaseData):
    """ it's a abstract class. """
    def __init__(self, file_url: str = None):
        self.file_url = file_url
        self.file_name = None
        self.file_type = None

    def get_url(self) -> str:
        """
        return the value of url.
        :return:
        """
        return self.file_url

    def get_file_name(self) -> str:
        """
        return the value of file_name.
        :return:
        """
        return self.file_name

    def get_file_type(self) -> str:
        """
        return the value of file_type.
        :return:
        """
        return self.file_type


class TxtData(FileData):
    pass


class CsvData(FileData):
    pass


class BaseHanding(ABC):
    """ this class is interface class. """
    def __init__(self, data: object):
        self.data = data
        self.dest_file_url = None


class DataHandling(BaseHanding):
    """ this class is abstract class. """
    @abstractmethod
    def convert_data(self):
        pass


class TextConvertToCsv(DataHandling):
    def __init__(self, url):
        self.obj = TxtData(url)

    def print_complete_data(self) -> None:
        """
        print the complete data.
        :return:
        """
        try:
            f = open(self.obj.file_url, 'r')
            print(f.read())
        except OSError as err:
            print(f'Cannot open: {err}')
            raise err
        except Exception as e:
            print(f'TextConvertToCsv class, print_complete_data(): ', e)
            raise e
        else:
            f.close()

    def set_dest_file_url(self, dest_file_url):
        self.dest_file_url = dest_file_url

    def convert_data(self) -> None:
        """
        convert data from txt to csv.
        :return:
        """
        if self.dest_file_url is not None:
            # with open(self.file_url, 'r') as file:
            #     pass
            # with open(self.file_url, 'w', newline='') as file:
            #     writer = csv.writer(file)
            #     for i in range(0, 10):
            #         writer.writerow([i, 'hello' + str(i)])
            pass


if __name__ == '__main__':
    url = '' # path of file.
    TextConvertToCsv(url)\
        .print_complete_data()




