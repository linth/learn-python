# import multiprocessing as mp
# from multiprocessing import Process
import time
import multiprocessing


# def cal_spend_time(func):
#     def swapper(num):
#         # print('num', num)
#         s = time.time()
#         func(num)
#         e = time.time()
#         print(e-s)
#     return swapper


def task(num):
    s = time.time()
    print('This is Process: ', num)
    e = time.time()
    print(e-s)
    

if __name__=='__main__':
    
    
    # num_process = 5
    # process_list = []
    
    # for i in range(num_process):
    #     process_list.append(Process(target=task, args = (i, )))
    #     process_list[i].start()

    # for i in range(num_process):
    #     process_list[i].join()
    
    print(multiprocessing.cpu_count()) # 4核心
    
    