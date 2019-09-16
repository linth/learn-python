'''
References:
    - https://blog.gtwang.org/programming/python-md5-sha-hash-functions-tutorial-examples/
'''
import hashlib

def get_md5_from_string():
    m = hashlib.md5()
    h = m.hexdigest()

    m1 = hashlib.md5()
    h1 = m.hexdigest()

    data = 'George'
    m.update(data.encode('utf-8')) # python 3

    print('The object of md5 is {}'.format(m)) # The object of md5 is <md5 HASH object @ 0x00000216AD7F0418>
    print('The value of hexdigest is {}'.format(h)) # The value of hexdigest is d41d8cd98f00b204e9800998ecf8427e

    data = 'May'
    m1.update(data.encode('utf-8')) # python 3

    print('The object of md5 is {}'.format(m1)) # The object of md5 is <md5 HASH object @ 0x00000216AD7F05A8>
    print('The value of hexdigest is {}'.format(h1)) # The value of hexdigest is 578ad8e10dc4edb52ff2bd4ec9bc93a3


def get_md5_from_file():
    file_name = 'test.txt'
    m = hashlib.md5()

    with open(file_name, 'rb') as f:
        buffer = f.read()
        m.update(buffer)

    h = m.hexdigest()
    print('The hexdigest of file is {}'.format(h)) # The hexdigest of file is 52a5375c48a077f0a4bb2841e81d909c


if __name__ == '__main__':
    get_md5_from_string()
    get_md5_from_file()
