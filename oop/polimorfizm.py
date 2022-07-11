"=============== Полиморфизм =============="
# Полиморфизм - принцип ООП, в котором методы в разных классах называются одинаково.(Один интерфейс - разный функционал)

class Dog:
    def speak(self):
        print('гав-гав')
        
class Cat:
    def speak(self):
        print("мяу-мяу")

class Frog:
    def speak(self):
        print('ква-ква')
        
animals= [Cat(),Dog(),Cat(),Frog(),Frog()]

for animal in animals:
    animal.speak()  #мяу-мяу
                    #гав-гав
                    #мяу-мяу
                    #ква-ква
                    #ква-ква


