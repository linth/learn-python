'''
    Reference:
    - https://blog.gtwang.org/programming/python-requests-module-tutorial/
    - http://docs.python-requests.org/en/master/
'''
import requests

# example 1: connect the website by using request.
def example1():
    res = requests.get("http://www.yahoo.com.tw/")
    print(res) # <Response [200]>
    print(res.status_code) # 200
    # print(res.text)


def check_the_status_connection(res):
    if res.status_code == 200:
        print("The status code is {}".format(res.status_code))

    # check_the_status_connection(res)


# example 2: add params to search.
def example2():
    my_params = {'key1': 'value1', 'key2': 'value2'}
    res2 = requests.get("https://www.youtube.com/", params=my_params)
    print('url', res2.url) # https://www.youtube.com/?key1=value1&key2=value2

# example 3: custom header.
# my_headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get('http://www.google.com/get', headers=my_headers)
# print(r.url) # http://www.google.com/get

# example 4: login, logout.
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print(r.url) # https://api.github.com/user


def get_information_by_url():
    res = requests.get('https://www.ptt.cc/bbs/index.html')
    # print('There are some functions which provide those functionalilities: {}.'.format(dir(res)))
    # 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url'
    # print(res.text) # get the html source code.
    print('The type of res is {}'.format(type(res)))
    print('The cookies of res is {}'.format(res.cookies))

    # add search parameters.
    # parameters = {'key1': 'value1', 'key2': 'value2'}
    return res



def main():
    get_information_by_url()

if __name__ == '__main__':
    main()
