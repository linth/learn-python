import asyncio
import time


class Task1:
    async def f1(self):
        print(f'class Task1: f1 function (before).')
        time.sleep(2)
        print(f'class Task1: f1 function (after).')
        return f'class Task1: f1 finished.'


class Task2:
    async def f2(self):
        print(f'class Task2: f2 function (before).')
        time.sleep(4)
        print(f'class Task2: f2 function (after).')
        return f'class Task2: f2 finished.'


class Task3:
    async def f3(self):
        print(f'class Task3: f3 function (before).')
        time.sleep(1)
        print(f'class Task3: f3 function (after).')
        return f'class Task3: f3 finished.'


class Task4:
    async def f4(self):
        print(f'class Task4: f4 function (before).')
        time.sleep(1)
        print(f'class Task4: f4 function (after).')
        return f'class Task4: f4 finished.'


class IeTask:
    @staticmethod
    async def run_task():
        return [
            asyncio.ensure_future(Task1().f1()),
            asyncio.ensure_future(Task3().f3()),
            asyncio.ensure_future(Task2().f2()),
            await Task4().f4(),
            await Task2().f2(),
        ]

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run_task())


if __name__ == '__main__':
    start = time.time()
    IeTask().run()
    end = time.time()
    print('spend time: ', end - start) # spend time:  8.001563787460327

    # import random
    # print(random.random() * 100)
