"================Exceptions==========="
# Исключения(ошибки) - обьекты , которые прерывают работу кода , если были вызваны
SyntaxError # исключения , которое выходит когда в коде дтопущена синтаксическая  ошибка 
# ( -SytaxError: unexpected EOF while parsing- когда мы забыли закрыть скобку или кавычку
# a =       - SyntaxError : invalid syntax (когда мы что то сделали не по синтаксису питона )

NameError # исключение, которое выходит ,когда мы обращаемся к несуществующей переменной 

# assakdask   - NameError: name 'assakdask'is not defined

IndexError # исключение которое выходит когда мы обращаемся по несуществующему индексу 
list_ = [1,2,3,4]
# list_[1000] - IndexError: list index output of range
# list_.pop[1000] - IndexError : pop index out of range

KeyError # исключение , которе выходит когда мы обращаемся по несуществующему ключу
dict_={'a':1}
# dict_['b'] - 


print(dict_.get('b')) # не ошибка, выйдет  None ,если ключа нет

# ValueError # Выходит когда мы пытаемся распаковать какую-то последовательность ,где количество переменных и
# a,b,c= 'ab' # ValueError: not enough values to unpack (expected 3 , got 2)
# a,b='ab'  # 2 символа могут распаковаться на 2 переменные 
# int('10d') # ValueError : invalid literal for int() with base 10: 10d

# TypeError # когда мы пытаемся использовать методы не свойственные какому-то типу данных или ,когда мы пытаемся передать в функцию больше или меньше аргументов,чем принимает функция

# for i in 1212148 # TypeError: "int" object is not iterable
# 5 + '5' # TypeError: unsupported operand type(s) for + : 'int' and 'str'
# '5' + 5 # TypeError : can only concatinate str (not 'int') to str
# hash([1,2]) # TypeError : unhashible type : 'list'
# {[1,2,3]:'hello'} # TypeError : unhashible type : 'list'
# input('hello', 1) # TypeError : input expected at most 1 argument , got 3
# [].append(1,2) # TypeError : append() takes exactly one argument (2,given)
# IndentationError # когда ,мы не правильно используем отступы
#     a = 4 # IntendationError : unexpected indent
# for i in range(3):
# print(i) # IntendationError : expected indent


# ZeroDivisionError # выходит при делении на ноль
# 45/0  # ZeroDivisionError : division by zero

# AttributeError # выходит когда мы обращаемся к к несущестувубщему аттрибуту или методу обьекта 

# "============= Обработка исключений==============="
# #  чтобы код не прекращал свою при неккоректных данных
# try: 
#     код который может вызвать ошибку
# except ошибка,которая может возниктнуть :
#     код, который сработает ,если в try ошибка вышла
# else :
#     код который сработает если в try ошибка не вышла
# finally:
#     код , который сработает в любом случае 

# try :
#     num = int(input())
# except ValueError:
#     print('введите число')
# else :
#     print('введенное число ', num)
# # если в input придет число - выйдет то, что мы напсиали в else 
# # если в input придет не число - выйдет  то что мы написали в except

# raise - вызвать ошибку 

# try :
#     raise SyntaxError
# except : # отловливает все ошибки
#     print('ыбла обработана ошибка')
