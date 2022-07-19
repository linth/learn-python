'''
packet & module

'''
from post.Post import Post

p = Post()
p.add_post('python')
p.add_post('java')

print(p.title)