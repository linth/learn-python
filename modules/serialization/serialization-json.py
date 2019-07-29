'''
Reference:
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017624706151424
    - https://ithelp.ithome.com.tw/articles/10187407

Keyword:
    - bytes
'''
import pickle
import json

def object_to_json_string():
    d = dict(name='Bob', age=20, score=90)
    print('The type of d is {}.'.format(type(d)))
    print('The d = {}'.format(d))

    # object => JSON (string)
    res = json.dumps(d) # return a string and JSON context.
    print('The type of res is {}'.format(type(res)))
    print('The res = {}'.format(res))

    # with open('json_dump.txt', 'wb') as data_file:
    #     json.dump(res, data_file) # return a string and JSON context.


# def json_string_to_file():
#     d = dict(name='Bob', age=20, score=90)
#     f = open('json_dump.txt', 'wb')
#     json.dump(d, f)
#     f.close()


def example():
    # JSON => write into the file.
    # f = open('json_dump.txt', 'wb')
    # json.dump(res, f)
    # f.close()
    pass

def example1():
    json_str = '{"age": 20, "score": 90, "name": "Bob"}'
    print('The type of json_str is {}.'.format(type(json_str))) # The type of json_str is <class 'str'>.
    print('The json_str = {}.'.format(json_str)) # The json_str = {"age": 20, "score": 90, "name": "Bob"}.

    # string (JSON) => dict (反序列化)
    res = json.loads(json_str)
    print('The type of res is {}.'.format(type(res))) # The type of res is <class 'dict'>.
    print('The res = {}.'.format(res)) # The res = {'age': 20, 'score': 90, 'name': 'Bob'}.

    # file-like object => dict (反序列化)


def example2():
    # object => JSON string.
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    res = json.dumps(data)
    print('The type of data is {}.'.format(type(data))) # The type of data is <class 'list'>.
    print('The type of res is {}.'.format(type(res))) # The type of res is <class 'str'>.
    print('The res = {}.'.format(res)) # The res = [{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}].

    res2 = json.loads(res)
    print('The type of res2 is {}.'.format(type(res2))) # The type of res2 is <class 'list'>.
    print('From res to res2, the res2 = {}'.format(res2)) # From res to res2, the res2 = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

    f = open('ex2-json.txt', 'wb')
    res2 = json.loads((res))
    f.close()


def example3():
    jsonData = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
    res = json.loads((jsonData))
    print('The type of res is {}.'.format(type(res)))

def main():
    # object_to_json_string()
    # json_string_to_file()
    # example1()
    example2()
    example3()

if __name__ == '__main__':
    main()
