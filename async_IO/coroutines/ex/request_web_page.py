'''
思考 request 多個 website 的任務。


'''
import asyncio
import requests
import time


async def send_request(url_list):
    t_start = time.time()
    
    for i in url_list:
        start = time.time()
        print(f"[task]: {i['task_name']}")
        
        response = requests.get(i['url'])
        print(response.status_code)
        
        end = time.time()
        print('task spending time', end-start)
    
    t_end = time.time()
    print('total tasks:', t_end - t_start)
    print('----------------')


def generate_data():
    # 產生3個資料
    url_list = []
        
    google = {
        'url': 'https://www.google.com',
        'task_name': 'google'
    }
    
    yahoo = {
        'url': 'https://www.yahoo.com',
        'task_name': 'yahoo'
    }
    
    youtube = {
        'url': 'https://www.youtube.com',
        'task_name': 'youtube'
    }
    
    url_list.append(google)
    url_list.append(yahoo)
    url_list.append(youtube)
    
    print(url_list)
    return url_list

# 在一個任務中，執行三個url訪問。
async def main():
    print('----------------------------')
    print('在一個任務中，執行三個url訪問。')
    print('----------------------------')
    start = time.time()
    
    l = generate_data()
    await asyncio.create_task(send_request(l))
    
    end = time.time()
    print(end - start)
    

# 將訪問三個url，分別獨立出變成三個任務。
async def main2():
    print('------------------------------------')
    print('將訪問三個url，分別獨立出變成三個任務。')
    print('------------------------------------')
    start = time.time()
    
    await asyncio.gather(
        send_request([{'url': 'https://www.google.com', 'task_name': 'google'}]),
        send_request([{'url': 'https://www.yahoo.com', 'task_name': 'yahoo'}]),
        send_request([{'url': 'https://www.youtube.com', 'task_name': 'youtube'}]),
    )
    
    # task1 = asyncio.create_task(send_request([{'url': 'https://www.google.com', 'task_name': 'google'}]))
    # task2 = asyncio.create_task(send_request([{'url': 'https://www.yahoo.com', 'task_name': 'yahoo'}]))
    # task3 = asyncio.create_task(send_request([{'url': 'https://www.youtube.com', 'task_name': 'youtube'}]))
        
    # await task1
    # await task2
    # await task3
    end = time.time()
    print(end - start)
    
asyncio.run(main())
asyncio.run(main2())