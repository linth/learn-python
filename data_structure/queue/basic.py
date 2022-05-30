"""
Reference
    - https://docs.python.org/3.8/library/queue.html
"""
import threading
import queue
from color.IeColor import IeColor


q = queue.Queue()


def worker():
    while True:
        item = q.get()
        print(IeColor.warning, f'working on {item}')
        print(IeColor.success, f'Finished {item}')
        q.task_done()


if __name__ == '__main__':
    # trun on the worker thread.
    threading.Thread(target=worker, daemon=True).start()

    # send thirty task requests to the worker.
    for item in range(30):
        q.put(item)
    print(IeColor.blue, 'All task requests sent\n', IeColor.end)

    print(IeColor.pink, f'size: {q.qsize()}', IeColor.end)

    # block until all tasks are done.
    q.join()
    print(IeColor.success, 'All work completed.')