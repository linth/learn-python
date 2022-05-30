"""
How to use classmethod in Python?

Reference:
    - None
"""
import os


class InputData(object):
    """ interface class. """
    def read(self):
        raise NotImplementedError('the read() must be overridden.')


class PathInputData(InputData):
    """ concrete subclass. """
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError('the map() must be overridden.')

    def reduce(self):
        raise NotImplementedError('the reduce() must be overridden.')


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


"""
Q: how to combine all above class?
A: use helper function. 
"""


def generate_input(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(workers):
    thread = [Thread(target=w.map) for w in workers]

    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result

