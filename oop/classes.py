"=================OOP================"
# OOP object oriented programming
# ООП обьектно ориетированное программирование(парадигма)
class Person:
    name = 'Бекзат'
    age = 20
    arms = 2
    legs = 2
    
    def walk():
        print('Я иду')
    def add_age(obj):
        obj.age += 1
# person1 = Person()
# print(person1.age) # 20
# print(person1.add_age()) # 21

class Person:
    arms = 2
    legs = 2
    
    def __init__(self, name, age):
        """
        функция которая вызывается когда мы создаем обьект от класса
        self -  ссылка на созданный обьект 
        """
        self.name = name # мы добавляем в обьект self новый аттритбут name
        self.age = age #nновый аттрибут age

    def add_age(self):
        self.age += 1
    def __str__(self):
        """ 
        Функция, которая вызывается, когда мы оборачиваем обьект в класс str или когда вызываем обьект
        функция __str__ ничего кроме self не принимает и обязательно должна возвращать строку
        """
        return self.name
person1 = Person('Бекзат', 4)
print(person1.age) # 4

"================ Аттрибуты класса =============="
# аттрибуты класса - переменные внутри класса


"================ Методы класса ================="
# методы класса - функции внутри класса

"================ Обьекты класса ================"
# обьект, экземпляр, instance класса - обьект созданный по шаблону класса (он перенимает все аттрибуты у класса)

"================ Аттрибуты и методы обьекта ===="
# аттрибуты и методы, которые есть у обьекта, но возможно их нет у класса

class A:
    var1 = "переменная класса"

    def __init__(self):
        self.var2 = "переменная обьекта"

# print(dir(A)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']

obj = A()
# print(dir(obj)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']

# print(A.var1) # переменная класса
# print(A.var2) # AttributeError: type object 'A' has no attribute 'var2'. Did you mean: 'var1'?

print(obj.var1) # переменная класса
print(obj.var2) # переменная обьекта

"Класс имеет доступ только к аттрибутам класса "
"Обьект имеет доступ к аттрибутам класса, и к аттрибутам этого самого обьекта"
