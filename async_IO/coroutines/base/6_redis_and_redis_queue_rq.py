'''
使用 Redis and Redis Queue RQ 範例



Reference:
    - https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb
'''
# from redis import Redis
# from rq import Queue 
# import requests

# def count_words_at_url(url):
#     """Just an example function that's called async."""
#     resp = requests.get(url)

#     print( len(resp.text.split()))
#     return( len(resp.text.split()))


# q = Queue(connection=Redis())
# job = q.enqueue(count_words_at_url, 'http://nvie.com')