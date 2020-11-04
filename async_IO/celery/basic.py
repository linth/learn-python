"""
Reference:
    - https://docs.celeryproject.org/en/stable/userguide/application.html
"""
from celery import Celery

# you can specify another name for the main module.
app = Celery('celery_example')
print(f'app, {app}')


@app.task
def add(x: int, y: int) -> int:
    return x + y


if __name__ == '__main__':
    print(f'app, {app.main}') # celery_example
    print(f'add, {add.name}') # celery_example.add
    
    # res = add.delay(1, 2)
    # print('-->', res)

