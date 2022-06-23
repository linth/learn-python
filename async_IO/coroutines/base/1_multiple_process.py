'''
使用 multiple-processing 範例

Reference:
    - https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb
'''
from multiprocessing import Process


def print_country(country='Asia'):
    print('The name of country is: ', country)
    

# 如果不輸入引數情況下
def not_args():
    p = Process(target=print_country)
    p.start()
    

# 如果有輸入引數情況下
def has_args():
    countries = ['America', 'Europe', 'Africa']
    
    for c in countries:
        p = Process(target=print_country, args=(c, ))
        p.start()        
        p.join()    


if __name__ == '__main__':
    # 如果不輸入引數情況下
    not_args()
    
    # 如果有輸入引數情況下
    has_args()
    
    '''
    The name of country is:  Asia
    The name of country is:  America
    The name of country is:  Europe
    The name of country is:  Africa
    '''