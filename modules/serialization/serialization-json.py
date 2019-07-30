'''
Reference:
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017624706151424
    - https://ithelp.ithome.com.tw/articles/10187407
    - https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/356804/

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
    name_emb = {'a':'1111','b':'2222','c':'3333','d':'4444'}
    print('The name_emb = {}, and the type of name_emb is {}.'.format(name_emb, type(name_emb))) # The name_emb = {'a': '1111', 'b': '2222', 'c': '3333', 'd': '4444'}, and the type of name_emb is <class 'dict'>.

    # json.dumps()用於將dict型別的資料轉成str
    jsObj = json.dumps(name_emb)
    print('The jsObj = {}, and the type of jsObj is {}.'.format(jsObj, type(jsObj))) # The jsObj = {"a": "1111", "b": "2222", "c": "3333", "d": "4444"}, and the type of jsObj is <class 'str'>.

    # json.loads()用於將str型別的資料轉成dict
    jsLoads = json.loads(jsObj)
    print('The jsLoads = {}, and the type of jsLoads is {}.'.format(jsLoads, type(jsLoads)))


def example4():
    name_emb = {'a':'1111','b':'2222','c':'3333','d':'4444'}

    # json.dump()用於將dict型別的資料轉成str，並寫入到json檔案中。
    # method 1.
    jsObj = json.dumps(name_emb)
    with open('example4.json', 'w') as f:
        f.write(jsObj)
        f.close()

    # method 2.
    json.dump(name_emb, open('example4.json', 'w'))


def example5():
    example5 = ('example4.json')
    # json.load()用於從json檔案中讀取資料。
    jsObj = json.load(open(example5))
    print('The jsObj = {}, and the type of jsObj is {}.'.format(jsObj, type(jsObj)))


def main():
    # object_to_json_string()
    # json_string_to_file()
    # example1()
    # example2()
    # example3()
    # example4()
    example5()

if __name__ == '__main__':
    main()
