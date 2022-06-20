'''
list + dict 範例

[
    {'id': 1, 'name': 'george'},
    {'id': 2, 'name': 'may'},
    {'id': 3, 'name': 'peter'},
    ...
]


Reference:
    - 
'''

def generate():
    l = []
    d1 = {'id': 1, 'name': 'george'}
    d2 = {'id': 2, 'name': 'may'}
    d3 = {'id': 3, 'name': 'peter'}
    
    l.append(d1)
    l.append(d2)
    l.append(d3)
    
    return l
    

res_l = generate()
print(res_l)


''' use object to do for-loop. '''
for i in res_l:
    print(i) # show dict data.


''' use index to do for-loop. '''
for i in range(len(res_l)):
    print(res_l[i])
    
    
    