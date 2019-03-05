'''
    Faker modules: generate data.

    Reference:
    - https://www.hjqjk.com/2017/Python-moudle-Faker.html
'''
from faker import Factory
from faker import Faker

# example 1: generate objects.
def example1():
    fake1 = Factory.create()
    print('fake1', fake1)

# example 2: generate data.
def example2():
    # address, person, barcode, color, company, credit_card, file , ..., etc.
    fake2 = Faker()

    name = fake2.name()
    address = fake2.address()
    text = fake2.text()

    print('name', name)
    print('address', address)
    print('text', text)

# example 2: change the lang.
def example3():
    fake3 = Faker("zh_CN")
    name3 = fake3.name()
    print(name3)

if __name__ == '__main__':
    example1()
    example2()
    example3()
