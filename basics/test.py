
# a = [title.split(' ')[i].lower() for i  in title.split(' ') if len(title.split(' ')[i]) <=2 for i in title.split(' ')]
# print(a)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list=["shorter" if len(x) <= 4  else "longer" for x in list_name]
# print(new_list)
# "leetcode -  Capitalize the Title"
# class Solution:
#     def capitalizeTitle(self, title: str) -> str:
#         return  ' '.join(title.split(' ')[x].lower() if len(title.split(' ')[x]) <=2 else title.split(' ')[x].title() for x in range(len(title.split(' '))))
# n = int(input( ))
# dict_= { k : k**2 for k in range(1,500) if k % n==0}
# print(dict_)


""" List, dictionary comprehension. Таск 13
# Дано предложение

#  string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# Получите список чисел list_ из этого предложения.

# Вывод будет таким:

# ['1984', '13', '1000'] 
# Нужно использовать comprehension.
"Решение"
string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
list_ = [string_.split()[k]for k in range(len(string_.split())) if string_.split()[k].isdigit()]
print(list_)"""



"""List, dictionary comprehension. Таск 14
Задание 14
Дан вложенный словарь dict_ (словарь состоящий из других словарей) в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам.

Распечатайте новый словарь, где вместо оценкок будет название предмета, по которому студент имеет высший балл. Нужно использовать comprehension.
"""

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},'Olga': {'history': 92, 'math': 96, 'literature': 81}, 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict= {k : k2 for k, v in dict_.items() for k2, v2 in v.items() if v2 == max(v.values()) }
# print(new_dict)

# List, Dict, Set comprehension. Экстра 2
# Экстра задание 2
# Создайте словарь dict_ в котором ключами будут числа, а значениями строки. Перебирите словарь циклом:

# если ключ четный, нужно заменить его значение на длину этого значения
# если ключ нечетный то возвести длинну его значения в 3 степень
# Распечатайте dict_.
"""dict_ ={1: 'AVD', 4:'asfsdf',3: 'cafb'}
print({k : len(v) if k%2==0 else len(v)**3 for k, v in dict_.items() }) """

# num1= int(input())
# num2= int(input())
# try:
#     print(num1/num2)
# except:
#     print("На ноль делить нельзя")
# dict_= {'key1': 'value1', 'key2':'value2'}
# try:
#     print(dict_['key1'])
# except:
#     print("Нет такого ключа!")
# try:
#     cash= int(input())
#     if cash<0:
#         raise ValueError ('Сумма не может быть отрицательной!')
# except:
#     print('Сумма не может быть отрицательно!')
# else:
#     print(cash)


"""Введение в ООП.
Задание 9
Создайте класс Math, у экземпляра которого должно быть свойство value. У классa Math должно быть 3 метода:

get_factorial - возвращает факториал числа(перемножить все составные числа до самого числа)

get_sum - возвращает сумму цифр числа

get_mul_table - возвращает таблицу умножения для числа до 10 в формате:
"""
class Math:
    def __init__(self, value):
        self.value = value

    def get_factorial(self):
        factorial = 1
        for i in range(2, self.value+1):
            factorial *= i
        return factorial

    def get_sum(self):
        suma = 0
        n = self.value
        while n > 0:
            digit = n % 10
            suma = suma + digit
            n = n // 10
        return suma

    def get_mul_table(self):
        table = ''
        for i in range(1, 11):
            table += f'{self.value}x{i}={self.value * i}\n'
        return table

num = Math(11)
num.get_factorial()
num.get_sum()
num.get_mul_table()

"""
Введение в ООП
Задание 8
Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:

В начале, проверьте, что пароль состоит из минимум 8 символов, но меньше 15, если условие не соблюдено, должны выйти ошибка с текстом:
Password should be longer than 8, and less than 15
Вторая проверка должна проверять что пароль содержит цифры, и в случае отсутствия цифр, выводить ошибку с текстом:
Password should contain numbers too
Третья проверка, проверяет содержит ли пароль буквы и в случае не совпадения, выводит ошибку с текстом:
Password should contain letters as well
В конце проверьте, содержит ли пароль хотя бы один из символов: '@', '#', '&', '$', '%', '!', '~', '*', если условие не выполнено выводите ошибку с текстом:
Your password should have some symbols
если одно из условий не выполнено, выводите соответствующее исключение, если же все условия выполнены метод validate должен возвращать строку:

Ваш пароль сохранен.
Также переопределите метод __str__, чтобы при попытке распечатать сам пароль, вам выдавалась строка из звездочек количество которых равно длине пароля.

К примеру, если пароль joe@123456, при попытке распечатать пароль, в терминал должно выводиться: **********

"""

class Password:
    def __init__(self, str_):
        self.str_ = str_

    def validate(self):
        if len(self.str_) < 8 or len(self.str_) >15:
            raise Exception ('Password should be longer than 8, and less than 15')
        
        elif not any(map(str.isdigit, self.str_)):
            raise Exception ('Password should contain numbers too')

        elif not any(map(str.isalpha, self.str_)):
            raise Exception ('Password should contain letters as well')

        check_symbol = list(filter(lambda x: x in '@#&$%!~*', self.str_))
        if len(check_symbol) == 0:
            raise Exception('Your password should have some symbols')
        
        else:
            return 'Ваш пароль сохранен.'

    def __str__(self):
        return len(self.str_) * '*'


pass1 = Password('aa#123456')
print(pass1.validate())
print(pass1)


"""
Введение в ООП.
Задание 10
Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д).

У класса должна быть переменная класса instances значением которой является пустой словарь.

Создайте внутри класса метод give_priority, который имеет параметр priority, куда принимает число - приоритет вашей задачи (1, 2, 3) и записывает вашу задачу в словарь instances с ключом в виде числа - priority, а значением в виде вашей задачи.

Например:

{3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

{1: 'сделать домашку'}
в этом случае это у вас самая важная задача, с приоритетом 1.

При каждом вызове метода give_priority - словарь в instances обновляется. Если вы создали три объекта от класса ToDo и к каждому объекту вызвали метод give_priority и дали приоритет, то ваш словарь в instances в конце будет выглядеть примерно так:

{3: 'сходить в кино', 1: 'сделать домашку', 2: 'выгулять собаку'} 
У класса должен быть метод list_of_tasks, который возвращает вам список отсортированных задач по приоритету:

[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]

"""



class ToDo:
    instances = {}

    def __init__(self, task):
        self.task = task

    def give_priority(self, priority):
        ToDo.instances[priority] = self.task

    def list_of_tasks(self):
        list_ = []
        for key, value in ToDo.instances.items():
            list_.append(tuple([key, value]))
        return sorted(list_)

todo1 = ToDo('Сделать домашку')
todo2 = ToDo('Сходить в кино')
todo3 = ToDo('Кормить кота')

todo1.give_priority(1)
todo2.give_priority(2)
todo2.give_priority(3)
print(ToDo.instances)
print(todo1.list_of_tasks())


"""
Создайте класс MyString, который будет наследоваться от str.

Определите 2 своих метода:

append, который будет принимать строку и добавлять её в конец исходной

pop, который удаляет из строки последний элемент и возвращает его.

Затем, создайте экземпляр example от класса MyString со значением String. Добавьте к example строку 'hello' методом append, затем примените метод pop.

"""
class MyString(str):
    def __init__(self, value):
        self.value = value
    
    def append(self, string):
        self.value += string

    def pop(self):
        string = self.value
        self.value = self.value[:-1]
        return string[-1]

    def __str__(self):
        return self.value

example = MyString('String') 
example.append('hello')
print(example) 
print(example.pop()) 
print(example) 


"""
Создайте класс ContactList, который должен наследоваться от встроенного класса list.

В вашем классе должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений.

Создайте экземпляр класса в переменной all_contacts и передайте список ваших контактов.

Примерный ввод:

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 
Метод search_by_name возвращает все строки содержащие подстроку "Olya":



"""

class ContactList(list):

    def __init__(self, value=list()):
        self.value = value

    def search_by_name(self, name):
        self.name = name
        list_ = []
        for i in self.value :
            if i.find(self.name) != -1:
                list_.append(i)
        return list_
all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 
    
            

"""
Принципы ООП. Наследование.
Задание 7
Создайте класс SmartPhones, экземпляры класса должны иметь такие свойства:

name - название
color - цвет
memory - память
battery - процент заряда батареи
Значение battery по умолчанию должно быть 0.

Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.

У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

Создайте два дочерних класса от Smartphones:

Iphone - с дополнительным аттрибутом экземпляра - ios и методом send_imessage(принимает в аргументы строку и возвращает эту строку и от какого телефона сообщение было выслано в таком формате - sending 'ваша строка' from 'название объекта-телефона')

Samsung - с дополнительным аттрибутом android и методом show_time(который показывает текущее время)

Создайте объекты phone, iphone7, samsung21 от классов SmartPhones, Iphone, Samsung и примените все методы.

Для правильной работы тестов, проделайте все следующие операции:

создайте объект от класса SmartPhones:

phone = SmartPhones('generic', 'blue', '128GB') 
print(phone) вывод:

generic 128GB
распечатайте свойство батарейки,затем примените метод charge(), зарядив телефон до 20%:

print(phone.battery) 
phone.charge(20) 
print(phone.battery) 
получим в терминале:

0 
20 
создайте объект от класс Iphone, распечатайте этот объект, и примените метод send_imessage:iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 
вывод будет:

Iphone 7 128gb 
sending hello from Iphone 7 128gb 
создайте объект от Samsung и примените метод show_time():

samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time()) 
вывод будет:

18:37:02.712036 
"""

class SmartPhones:
    def __init__(self, name, color, memory, battery = 0):
        self.name = name
        self.color = color
        self.memory = memory
        self.battery = battery

    def __str__(self):
        return f'{self.name} {self.memory}'

    def charge(self,power):
        if power <= 100 and power > 0:
            self.battery += power
            return self.battery
        
        elif power >100:
            self.battery += 100

        elif power < 0 :
            raise Exception ('ChargeError')

class Iphone(SmartPhones):
    def __init__(self, name, color, memory,OS, battery = 0):
        super().__init__(name, color, memory, battery)
        self.OS = OS

    def send_imessage(self, message):
        return f'sending {message} from {self.name} {self.memory}'

class Samsung(SmartPhones):
    def __init__(self, name, color, memory, OS, battery = 0) :
        super().__init__(name, color, memory, battery)
        self.OS = OS

    def show_time(self):
        from datetime import datetime
        current_time = datetime.now()
        return current_time.time()
        

phone = SmartPhones('generic', 'blue', '128GB') 
print(phone) 

print(phone.battery) 
phone.charge(20) 
print(phone.battery) 

iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 


samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time())


"""
Принципы ООП. Наследование.
Задание 8
Напишите класс CustomError который наследуется от встроенного класса исключений Exception.

Переопределите __init__ таким образом чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.

Создайте исключение от этого класса в переменной capitals_error с сообщением:

ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ
Напишите функцию check_letters(вне класса, отдельно от класса), проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом CustomError:

Если же все хорошо необходимо вывести сообщение: ВСЕ ОТЛИЧНО! {ваша строка}.

"""
class CustomError(Exception):
    def __init__(self, error):
        self.error = error

def check_letters(str_):
    if not str_.isupper():
        raise capitals_error
    else :
        return f'ВСЕ ОТЛИЧНО! {str_}'

capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
print(check_letters("HELLo")) 


"""
Принципы ООП. Полиморфизм.
Задание 3
Создайте 3 класса: Person с параметрами name и last_name, Employee с work и status, Student c university и course, при этом Employee и Student должны наследоваться от Person.

Определите во всех трёх классах метод get_info():

для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.

для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании Рога и копыта на должности директор.

для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.

Вне класса, определите функцию get_human_info(), которая будет принимать объект одного из трёх классов и вызывать у него метод get_info и распечатывать результат этой функции.
Создайте для каждого класса по экземпляру, для Person экземпляр person, для Employee экземпляр employee и student для класса Student.

Вызовите метод get_human_info у каждого экземпляра печатать результат.

Ввод должен быть:

get_human_info(employee) 
get_human_info(student) 
get_human_info(person) 
"""
class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_info(self):
        return f'Привет, меня зовут {self.name} {self.last_name}'

class Employee(Person):
    def __init__(self, name, last_name, work, status):
        super().__init__(name, last_name)
        self.work = work
        self.status = status
    
    def get_info(self):
        return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}'

class Student(Person):
    def __init__(self,name, last_name, university, course):
        super().__init__(name, last_name)
        self.university = university
        self.course = course

    def get_info(self):
        return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе'
    
def get_human_info(obj):
    print(obj.get_info())

person = Person("Иван", "Петров")
employee = Employee("Иван", "Петров", "Рога и копыта", "директор")
student = Student("Иван", "Петров","КГТУ", "3")

get_human_info(employee)
get_human_info(student)
get_human_info(person)