class Dog:
    def voice(self):
        print('Гав- гав')

dog = Dog()
dog.voice() # Гав- гав

class Cat:
    def voice(self):
        print("Мяу")
kity = Cat()
kity.voice() #  Мяу

# from abc import ABC, abstractmethod, abstractproperty

# class AbstractAnimal(ABC):
#     has_heart = True

#     @abstractmethod
#     def live(self):
#         pass


# class Dog(AbstractAnimal):
#     def live(self):
#         print('hrllo')

# dog = Dog()
# print(dog.live)














# class RadioMixin:
#     def play(self):
#         print('Playing music')


# class Car(list, RadioMixin):
#     pass

# class Boat:
#     pass










# class Person:
#     name = 'Nastya'

#     @staticmethod
#     def create_person():
#         pass

# person = Person()
# print(person.create_person())








# import json


# python_obj = [{'name': 'Nastya'}, 1, 2, 3]

# print(json.dumps(python_obj))