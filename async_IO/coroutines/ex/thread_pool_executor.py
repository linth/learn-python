'''
concurrent.futures — 創立非同步任務


concurrent.futures 提供了一組高階 API 給使用者操作非同步執行的任務。
    - 透過 ThreadPoolExectuor 執行 thread 層級的非同步任務。
    - 使用 ProcessPoolExecutor 執行 process 層級的非同步任務。
兩者的 API 介面都相同，同樣繼承於 Executor。



Reference:
    - https://blog.louie.lu/2017/08/01/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-06-concurrent-futures/
    - https://docs.python.org/3/library/concurrent.futures.html
'''
import concurrent.futures
import requests
import time


URLS = [
    'https://docs.python.org/3/library/ast.html',
    'https://docs.python.org/3/library/abc.html',
    'https://docs.python.org/3/library/time.html',
    'https://docs.python.org/3/library/os.html',
    'https://docs.python.org/3/library/sys.html',
    'https://docs.python.org/3/library/io.html',
    'https://docs.python.org/3/library/pdb.html',
    'https://docs.python.org/3/library/weakref.html'
]
 
 
def get_content(url):
    return requests.get(url).text
 
 
def scrap(mw=5):
    with concurrent.futures.ThreadPoolExecutor(max_workers=mw) as executor:
        future_to_url = {
            executor.submit(get_content, url): url for url in URLS
        }
        
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            
            try:
                data = future.result()
            except Execption as exc:
                print(f'\'{url}\' generated an exception: {exc}')
            else:
                print(f'\'{url}\' page length is {len(data)}')
 
 
def main():
    for url in URLS:
        try:
            data = get_content(url)
        except Exception as exc:
            print(f'\'{url}\' generated an exception: {exc}')
        else:
            print(f'\'{url}\' page length is {len(data)}')
 
 
if __name__ == '__main__':
    # 使用 ThreadPoolExecutor，worker = 5
    s = time.time()
    scrap()
    e = time.time()
    print('total time:', e-s)
    
    s = time.time()
    scrap(10) # worker = 5
    e = time.time()
    print('total time:', e-s)
    
    
    # 使用一個一個抓取資料方式 
    main_s = time.time()
    main()
    main_e = time.time()
    print('total time:', main_e-main_s)
    
    '''
    使用 ThreadPoolExecutor 
    total time: 0.48400115966796875

    使用一個一個抓取資料方式 
    total time: 1.587104320526123
    
    速度效能快上4倍速的時間。
    '''