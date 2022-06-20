'''
python module: click.
    - 學習如何使用 click module.

Reference:
    - https://click.palletsprojects.com/en/8.1.x/
'''
import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    for x in range(count):
        click.echo(f'Hello {name}!')


if __name__ == '__main__':
    
    # python hello.py --count=3 Your name: John
    hello()
    