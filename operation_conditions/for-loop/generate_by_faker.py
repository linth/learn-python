from faker import Faker

f = Faker('zh_TW')
l = []

d = {
    'name': None,
    'address': f.address(),
    'date': f.date(),
}

for i in range(10):
    d['name'] = f.name()
    d['address'] = f.address()
    d['date'] = f.date()
    l.append(d)
    d = {}

print(l)



