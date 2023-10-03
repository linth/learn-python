'''
user case: scheduling with composite aggregate reuse.

'''


class Task:
  
    def __init__(self, name, priority) -> None:
        self.name = name
        self.priority = priority
        
    def execute(self) -> None:
        print(f'executing task: ${self.name}')
        
        
class Scheduling:
    def __init__(self) -> None:
        self.tasks = []
        
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        
    def schedule(self) -> None:
        pass
      
      
class FCFS_scheduling(Scheduling):
  
    def schedule(self) -> None:
        print("Scheduling tasks using First-Come, First-Served (FCFS) algorithm:")
        
        for task in self.tasks:
            task.execute()
            
            
class RR_scheduling(Scheduling):

    def __init__(self, time_slice) -> None:
        super().__init__()
        self.time_slice = time_slice
        
    def schedule(self) -> None:
        print(f'Scheduling tasks using Round Robin (RR) algorithm with time slice {self.time_slice}:')
        
        while self.tasks:
            task = self.tasks.pop(0)
            task.execute()
            self.tasks.append(task)
            

class Priority_scheduling(Scheduling):
  
    def schedule(self) -> None:
        print('Scheduling tasks using Priority algorithm:')
        sorted_tasks = sorted(self.tasks, key=lambda x: x.priority)
        for task in sorted_tasks:
            task.execute()
            
            
if __name__ == "__main__":
    task1 = Task("Task 1", 3)
    task2 = Task("Task 2", 1)
    task3 = Task("Task 3", 2)

    fcfs_scheduler = FCFS_scheduling()
    fcfs_scheduler.add_task(task1)
    fcfs_scheduler.add_task(task2)
    fcfs_scheduler.add_task(task3)
    fcfs_scheduler.schedule()

    rr_scheduler = RR_scheduling(2)
    rr_scheduler.add_task(task1)
    rr_scheduler.add_task(task2)
    rr_scheduler.add_task(task3)
    rr_scheduler.schedule()

    priority_scheduler = Priority_scheduling()
    priority_scheduler.add_task(task1)
    priority_scheduler.add_task(task2)
    priority_scheduler.add_task(task3)
    priority_scheduler.schedule()
