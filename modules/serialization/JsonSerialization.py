"""
Serialization, marshalling, flattening.

將一個 object 序列化轉換成 bytes，後續可以將 bytes 寫入文件。
或是用另一方法 `pickle.dump()` 直接把 object 序列化寫入一個 file-like Object.

序列化:
    - object -> bytes
        - dumps()
    - object -> file-like object
        - dump()
反序列化:
    - bytes -> object
        - loads()
    - file-like object -> object
        - load()

Reference:
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017624706151424
    - https://docs.python-guide.org/scenarios/serialization/
    - https://ithelp.ithome.com.tw/articles/10187407
"""
import pickle
import json


def object_to_bytes(data: dict):
    """
    object convert to bytes.
    :param data:
    :return:
    """
    return pickle.dumps(data)


def object_to_file(data: dict, file_path : str = None):
    """
    object convert to file-like object.
    :param file_path:
    :param data:
    :return:
    """
    try:
        if file_path is None:
            file_path = 'dump.txt'
        f = open(file_path, 'wb')

        if f:
            pickle.dump(data, f)
            f.close()
            return f'successful'
        else:
            return f'failure'
    except Exception as e:
        raise e


def bytes_to_object(data: dict):
    """
    bytes convert to object in memory.
    :param data:
    :return:
    """
    return pickle.loads(data)


def file_to_object(file_path: str = None):
    """
    file-like convert to object in memory.
    :param file_path:
    :return:
    """
    if file_path is None:
        file_path = 'dump.txt'
    f = open(file_path, 'rb')
    d_ = pickle.load(f)
    f.close()
    return d_


if __name__ == '__main__':
    d = dict(name='Bob',
             age=33,
             socre=100)

    # #####################################
    # pickle example
    # #####################################
    # object => bytes.
    # TODO: check the meaning for bytes.
    o2b = object_to_bytes(d)
    print(f'result: {o2b}; the type: {type(o2b)}')

    # bytes => object.
    b2o = bytes_to_object(o2b)
    print(f'result: {b2o}; the type: {type(b2o)}')

    # object 轉成 file.
    o2f = object_to_file(d)
    print(f'result: {o2f}; the type: {type(o2f)}')

    f2o = file_to_object()
    print(f'result: {f2o}; the type: {type(f2o)}')

    # #####################################
    # Json example.
    # #####################################
    # object 轉成 json.
    o2j = json.dumps(d)
    print(f'(object => json) result: {o2j}; the type: {type(o2j)}')

    # object 轉成 file.
    with open('json.json', 'w') as file_json:
        j2f = json.dump(d, file_json)
        print(f'(json => file) result: {j2f}; the type: {type(j2f)}')

    # json 轉成 object.
    j2o = json.loads(o2j)
    print(f'(json => object) result: {j2o}; the type: {type(j2o)}')

    # file 轉成 object.
    """ [注意] 如果不使用`with open` 上面範例同時使用 json.json會有衝突意外發生。 """
    with open('json.json', 'r') as read_json_file:
        if read_json_file:
            f2o = json.load(read_json_file)
            print(f'(file => object) result: {f2o}; the type: {type(f2o)}')





