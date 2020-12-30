"""
Goal:
    - learn json concept.

data type:
    - Python:
        1) dict
        2) list
        3) str
        4) int
        5) float
        6) True
        7) False
        8) None
    - JSON:
        1) object
        2) array
        3) string
        4) number (int)
        5) number (real)
        6) true
        7) false
        8) null

function:
    - decode: the data type is changed from JSON to Python.
        - json.load()
        - json.loads()
    - encode: the data type is changed from Python to JSON.
        - json.dump()
        - json.dumps()

Reference:
    - https://pymotw.com/3/json/index.html
    - https://ithelp.ithome.com.tw/articles/10216970
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
