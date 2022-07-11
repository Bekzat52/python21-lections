"============= Принцип ООП ============="
#Инсапсуляция - принцип ООП 
# 1. сокрытие данных (ограничение доступа к ограниченным методам и классам)
# 2. сбор всех необходимых для класса методов и аттрибутов в "капсулу" (класс)


"============= Модификаторы доступа к аттрибутам ===================="
# 1. public
# 2. protected
# 3. private
class A:
    attr1 = 'публичный'
    _attr2 = "защищенный"
    __attr3 = 'приватный'

A.attr1 # публичный
A._attr2 # защищенный
# A.__attr3 # AttributeError: type object 'A' has no attribute '__attr3'. Did you mean: '_A__attr3'?
A._A__attr3 # приватный


"=========== getter / setter ================"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

obj = Person('Настя', 18)
# print(obj.__age) # AttributeError: 'Person' object has no attribute '__age'

print(obj.get_age()) # 18
print(obj.get_age) #  <bound method Person.get_age of <__main__.Person object at 0x7ff9c7077fd0>>

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 120 and new_age >0:
            self.__age = new_age
        else:
            raise Exception('age can not be less than 0 or more than 120')

obj = Person('Настя', 18)
print(obj.age) # 18
obj.age = 5
print(obj.age) # 5

