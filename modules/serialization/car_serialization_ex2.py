'''
user case: car class for serialization.

'''

import pickle

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def __str__(self):
        return f"{self.make} {self.model}"
        
    def __repr__(self):
        '''
            The __repr__() method in Python is used to return a string that can be used to recreate the object. 
            It should return a string that, when passed to eval(), will produce a new object with the same value as the original object.
            
            The __repr__() method is typically used to generate a string representation of an object that can be used for debugging and development purposes. 
            When a programmer is trying to understand the state of an object or how it was created, they can use the string returned by __repr__() to recreate the object and inspect its attributes.
        '''
        return f"Car('{self.make}', '{self.model}')"

if __name__ == '__main__':
    ''' a car object example. '''
    # create a Car object
    my_car = Car('Toyota', 'Corolla')

    # serialize the object to a file using pickle
    with open('modules/serialization/my_car.pickle', 'wb') as f:
        pickle.dump(my_car, f)

    # deserialize the object from the file using pickle
    with open('modules/serialization/my_car.pickle', 'rb') as f:
        my_car = pickle.load(f)

    print(my_car)   # output: Toyota Corolla



    ''' several car objects example. '''
    # create a list of Car objects
    cars = [Car('Toyota', 'Corolla'), Car('Honda', 'Accord'), Car('Tesla', 'Model S')]

    # serialize the list of objects to a file using pickle
    with open('modules/serialization/cars.pickle', 'wb') as f:
        pickle.dump(cars, f)

    # deserialize the list of objects from the file using pickle
    with open('modules/serialization/cars.pickle', 'rb') as f:
        cars = pickle.load(f)

    # print each car object in the deserialized list
    for car in cars:
        print(car)






