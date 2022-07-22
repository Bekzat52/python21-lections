"================== Области видимости и пространства имен================"
locals() # -  возвращает словарь со всеми локальными переменненными
globals() # - возвращает словарь со всеми глобальными  переменненными

# LEGB - local,enclosed,global,build-in
" Built-in "  # встроенное пространство имен (все пространственные переменные(print,input,sum,max,min,len,abs,int,str,dict...))

# Globals - глобальные пространство имен  ( все переменные внутри файла, которые создали мы )

# чтобы узнать ,что находится в глобальном пространстве ,можно испольщовать функцию globals()
" Enclosed " # это прострванство находящееся между двумя пространствами
"Local"  # какое то закрытое пространство
# count = 0 
# def add():
#     global count # 
#     print(count)
#     count += 1 
# add ()
# add ()
# add () 
# print(count)   
# # 0 1 2 3 
# count = 0 
# def add():
#     global count
#     count += 1
#     print(count)
# add ()
# add ()
# add () 
# print(count) 
# # 1 2 3 3 
# a = "global"
# def outer_func():
#     a= "enclosed"
    
#     def inner_func():
#         a = 'local'
#         print(a)
#     print(a)
# print(a)
# outer_func()    
# # global enclosed
# a = "global"
# def outer_func():
#     a= "enclosed"
    
#     def inner_func():
#         a = 'local'
#         print(a)
#     print(a)
# print(a)
# outer_func() 
# inner_func() 
# #global  enclosed NameError


# def count(i) :
#     counter= 0

#     def add():
#         nonlocal counter # доступ на чтение и изменение локальной перемнной counter 
#         print(counter)
#         counter += 1
#     for  _ in range(i):
#         add()
# count(10)
# # 0 1 2 3 4 5 6 7 8 9

# sum = 5
# def func():
#     sum = 10
#     def inner_func():
#         sum = 20
#         def inner2__func():
#             sum = 30
#             print(sum)
#         inner2_func()
#     inner_func()
# func()

# def func(*args):
#     f = len(args)
#     languages = []
#     if f>1:
#         while f != 0:
#             languages.append(args[f-1])
#             f -= 1
#     languages.reverse()
#     c = str(languages).replace(',', ' and').replace('[', '').replace(']', '')
#     print(c)

# func(1,2,3,5,7, 8)


from abc import ABC,abstractmethod
class Coder(ABC):
    count_code_time = 0

    @abstractmethod
    def get_info(self):
        ...

    @abstractmethod
    def coding(self):
        ...

class Backend(Coder):
    def __init__(self, experience, *languages_backend):
        self.experience = experience
        self.languages_backend = languages_backend

    
    def get_info(self):
        f = len(self.languages_backend)
        if f>1:
            for i in range(f):

                return f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time}"
        else:
            return f"{self.languages_backend[0]} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"

    def coding(self, coding_hours):
        self.count_code_time += coding_hours


class Frontend(Coder):
    def __init__(self, experience, *languages_frontend):
        self.experience = experience
        self.languages_frontend = languages_frontend

    def get_info(self):
        f = len(self.languages_frontend)
        for i in range(f):
                str_ = list(self.languages_frontend)
                str2 = self.languages_frontend[i-1]
        if f>1:
            return f"{str2} разработчик, уровень: {self.experience}, потрачено {self.count_code_time}"
        else:
            return f"{self.languages_frontend[0]} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"




    def coding(self, coding_hours):
        self.count_code_time += coding_hours

class Fullstack(Frontend, Backend):
    ...

a = Backend('Senior', 'Ruby')
b = Frontend('Junior', 'C++')
c = Fullstack('Ultra mega super puper senior', 'HTML', 'python')
a.coding(100)
b.coding(520)
c.coding(87946532)
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info()) 





