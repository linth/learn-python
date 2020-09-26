"""
Reference:
    - https://pymotw.com/3/json/index.html
"""
import json


data = [{'a': 'A', 'c': 3.0, 'b': (2, 4),}]
print('data: ', repr(data), type(data))

# encoded
data_string = json.dumps(data)
print('json: ', data_string, type(data_string))

# decoded
decoded = json.loads(data_string)
print('decoded: ', decoded, type(decoded))

# please check the type of data.
print('original: ', type(data[0]['b']))
print('decoded: ', type(decoded[0]['b']))


unsorted = json.dumps(data)
_sorted = json.dumps(data, sort_keys=True)
print('unsorted: ', unsorted)
print('sorted: ', _sorted)
