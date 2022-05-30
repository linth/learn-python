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
for i in dict.keys():
    # show keys.
    print('keys = ', i) # name, year, sex, weight, height.

for x in dict.values():
    # show value.
    print('values = ', x) # George, 2000, boy, 78, 190.

for x, y in dict.items():
    print(x, y) # name George, year 2000, sex boy, weight 78, height 190.

# copy dictionary
x = dict.copy()
print(x) # {'name': 'George', 'year': 2000, 'sex': 'boy', 'weight': 78, 'height': 190}

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

z = dict.clear() # remove all data.
print(z) # return None.

# remove the lastinserted item
dict = {"year": 2019, "sex": "boy", "weight": 78, "height": 190}
dict.popitem()
print(dict) # year 2019, sex boy, weight 78

# remove the specified key name.
del dict['year']
print(dict) # sex boy, weight 78

# update, merge two dict
# it's for python 2.x and it's not support to python 3 up.
# dict1 = {"name": "George", "id": 1234}
# dict2 = {"name": "Peter", "id": 3456}
# print(dict1.update(dict2))
