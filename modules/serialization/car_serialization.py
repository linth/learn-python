'''
car user case for serialization.

Reference:
  - https://learnpython.com/blog/object-serialization-in-python/
'''
import pickle

class Car:
  def __init__(self, efficiency, fuel_level) -> None:
    self.efficiency = efficiency
    self.fuel_level = fuel_level
    
  # 方法 1: using __iter__() method.
  def __iter__(self):
    return iter([self.efficiency, self.fuel_level])
  
  # 方法 2: using __getitem__() method.
  def __getitem__(self, index):
    if index == 0:
      return self.efficiency
    elif index == 1:
      return self.fuel_level
    else:
      raise IndexError('index out of range')

  def drive(self, distance):
    max_distance = self.fuel_level * self.efficiency
      
    if distance > max_distance:
      print('Traveled %s km, out of fuel'%(max_distance))
      self.fuel_level = 0
    else:
      self.fuel_level -= distance / self.efficiency
      print('Arrived safely!')



if __name__ == '__main__':
  fast_car1 = Car(5, 12)
  print(fast_car1.efficiency)
  print(fast_car1.fuel_level)
  
  fast_car3 = Car(6, 13)
  fast_car4 = Car(7, 14)
  
  with open('modules/serialization/fast_car_object.pkl', 'wb') as out_file:
    pickle.dump(fast_car1, out_file)
    
  # with open('modules/serialization/fast_car_object.pkl', 'rb') as in_file:
  #   fast_car2 = pickle.load(in_file)
  #   for i in fast_car2:
  #     print(i)
      
  for item in fast_car3:
    print(item)