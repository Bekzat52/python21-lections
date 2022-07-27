# import random
# a = input('Ваше имя :',)
# b = input("Хотите играть? -",)
# t = 1
# c = random.randint(3, 5)
# print(c)
# while str(b) == 'нет': 
#     break
# d = (input('Угадайте число:', ))
# if int(d)== c:
#     print(f'ВЫ УГАДАЛИ ЧИСЛО!\nКОЛИЧЕСТВО ПОПЫТОК : {t} ')     
# while int(d) != c :
#         v =input('Попробуйте заново:',)
#         t =t+1
# if int(v) ==c :
#             print(f'ВЫ УГАДАЛИ ЧИСЛО!\nКОЛИЧЕСТВО ПОПЫТОК : {t} ')

# import datetime
# now = datetime.datetime.now()

# print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))

# from more_itertools import value_chain

# dict5 = {"a":3}
# dict5.update(key = 'value')
# print(dict5)

'''
Множественное наследование и миксины.
Задание 6
Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.

У класса должен быть один метод set_deadline, который принимает дату дедлайна (в виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.

Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:

в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key по которому нужно добавить задачу в словарь todos, если ключ уже существует верните "Задача под таким ключём уже существует".

класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который передается как аргумент, и возвращаетсообщение 'удалили название задачу', где вместо слова название должно быть название задачи.

класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое значение new_value и заменяет задачу под данным ключом на новое значение.

класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.


'''

# class CreateMixin:
#     def create(self, key, todo):
#         if key in self.todos.keys():
#             return'Задача под таким ключём уже существует'
#         else:
#             self.todos[key] = todo
#             return self.todos

# class DeleteMixin:
#     def delete(self, key):
#         if key in self.todos.keys():
#             return self.todos.pop(key)
#         else:
#             return 'KeyError'

# class UpdateMixin:
#     def update(self, key, new_value):
#         if key in self.todos.keys():
#             self.todos[key] = new_value
#             return self.todos
#         else: 
#             return 'KeyError'

# class ReadMixin:
#     def read(self):
#         res = [x for x in self.todos.items()]
#         return sorted(res)

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    
#     def __init__(self):
#         self.todos = {}


#     def set_deadline(self, date):
#         from datetime import datetime
#         l = date.split('/')
#         date1 = datetime.today()
#         date2 = datetime(day=int(l[0]), month=int(l[1]), year=int(l[2]))
#         timedelta = date2 - date1
#         l = timedelta.days +1
#         return l

