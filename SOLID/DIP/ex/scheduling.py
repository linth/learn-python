'''
user case: scheduling example

'''
from abc import ABC, abstractmethod

class IScheduler(ABC):
    ''' interface for scheduling. '''
    @abstractmethod
    def schedule_task(self, task):
        pass
      
      
class FCFS(IScheduler):
    ''' scheduling for FCFS. '''  
    def schedule_task(self, task):
        print(f'Scheduled task ${task} using First-Come, First-Served (FCFS) scheduling')
        return super().schedule_task(task)
    
    
class RoundRobin(IScheduler):
    ''' scheduling for RR. '''
    def schedule_task(self, task):
        print(f'Scheduled task ${task} using Round Robin scheduling')
        return super().schedule_task(task)
      
      
class Priority(IScheduler):
    ''' scheduling for priority. '''
    def schedule_task(self, task):
        print(f'Scheduled task ${task} using Priority scheduling')
        return super().schedule_task(task)
      
      
class TaskManager:
    def __init__(self, schedular: IScheduler) -> None:
        self.scheduler = schedular
        
    def add_task(self, task):
        self.scheduler.schedule_task(task)
        
        
if __name__ == '__main__':
    fcfs = FCFS()
    rr = RoundRobin()
    ps = Priority()
    
    task_manager = TaskManager(fcfs)
    task_manager.add_task('task 1')
    
    task_manager = TaskManager(rr)
    task_manager.add_task('task 2')
    
    task_manager = TaskManager(ps)
    task_manager.add_task('task 3')