# dictionary: key and value.

dict = {
    "name": "George",
    "year": 2019,
    "sex": "boy",
    "weight": 78,
    "height": 190,
}
print(dict)

# get value
print(dict['year']) # first way to get value.
x = dict.get('year') # another way to get value.
print(x) # 2019.

# change value
dict['year'] = 2000
print(dict['year']) # 2000.

# use for loop to show data
for i in dict:
    # show key.
    print(i) # name, year, sex, weight, height.

for x in dict.values():
    # show value.
    print(x) # George, 2000, boy, 78, 190.

for x, y in dict.items():
    print(x, y) # name George, year 2000, sex boy, weight 78, height 190.

# add items.
dict = {
    "name": "George",
    "year": 2019,
    "sex": "boy",
    "weight": 78,
    "height": 190,
}
dict['name'] = 'Peter'
print(dict) # name Peter, year 2019, sex boy, weight 78, height 190.

# remove item
dict.pop('name')
print(dict) # year 2019, sex boy, weight 78, height 190.

# remove the lastinserted item
dict.popitem()
print(dict) # year 2019, sex boy, weight 78

# remove the specified key name.
del dict['year']
print(dict) # sex boy, weight 78
