"================ Абстракция ============="
# Абстракция - Принцип ООП, в котором создается абстрактный класс (класс -пустышка), в котором задаются названия аттрибутов и методов, для того, чтобы в дочерних классах переопределить их нужным образом. От абстрактных классов мы не создаем обьекты , потому что в них только названия и нет логики.

from abc import ABC, abstractmethod, abstractproperty, abstractproperty

class AbstractAnimal(ABC):
    @abstractmethod
    def voice(self):
        ...

    @abstractproperty
    def legs(self):
        ...

# obj = AbstractAnimal() # TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

class Dog(AbstractAnimal):
    ... 

obj = Dog() # TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

class Dog(AbstractAnimal):
    legs = 4
    def voice(self):
        print('гав - гав')

class Cat(AbstractAnimal):
    legs = 4
    
    def voice(self):
        print('мяу - мяу')

dog1 = Dog()
dog1.voice() # гав - гав

cat1 = Cat()
cat1.legs # 4

Cat.шерсть = "рыжая"
print(cat1.шерсть) # рыжая
