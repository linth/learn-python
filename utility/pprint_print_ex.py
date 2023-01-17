'''
pprint vs. print

Reference:
    - https://www.maxlist.xyz/2022/10/06/python-pprint/
'''
import pprint
 
user_info = [
    {
        "userId": 1,
        "id": 1,
        "userInfo": {
            "userName": "Max",
            "email": "a0025071@gmail.com",
            "website": "https://www.maxlist.xyz/",
        },
    },
    {
        "userId": 2,
        "id": 2,
        "userInfo": {
            "userName": "Foo",
            "email": "foo@gmail.com",
            "website": "https://www.maxlist.xyz/",
        },
    },
]
 
pprint.pprint(user_info)