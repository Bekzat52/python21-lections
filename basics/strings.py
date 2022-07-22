"===========Строки=================="
# строки -  неизменяемыйтип данных который предназначен для хранения текстов или (последовательности символов),заключенного в одинарные или двойные ковычки
# синтаксис :
from os import sep
import string
from tkinter import CENTER


string1='строка с одинарными ковычками'
string2="строка с двойными ковычками"
# error =' неправильная строка"
string3 = "don't" # внутри двойных ковычек все одинарные- просто символы
string4= '"Makers bootcamp"' # внутри одинарных ковычек все двойные -просто символы
string5= ''' многосторчный текст
в одинарных ковычках
Тут можно ставить "любые" 'ковычки' 
'''
string6 = """
Многострочный текст 
в двойных кавычках
Тут можно ставить "любые" 'кавычки'
'''''
"""
string7= 'hello'+ ' ' + 'world' # 'hello world'
string* 'A'*5 # 'AAAAA'
"===================Экранизация строк============="
# экранизация спец.символов 
'\n' # перенос на новую строку
'\t' # табуляция
'\\' # Отображение -(\) ,потому что (\) является инструкцией,которая влияет на наш код
'\'' # отображение (')
"\"" # отображение (")
'\r' # возвращение каретки начало строки
'\v' # перенос на новую строку с смещением вправо на длину преидущей строки 


'hello\nworld'
''' 
hello
world
'''


'hello\tworld'
# hello    world

'чтобы экранировать нужен символ \\'
# чтобы эранировать нужен символ \
'My website is Latracal \rSolution'
# Solutionte is Latracal


'hello\vworld'
#hello
#     world

"============= Форматирование строк =================="
title='Плов'
price=1500
f' Название: {title},Цена {price}'
# Название: Плов , Цена : 1500
# {} фигурные скобки вместе с 'f' делают строки динамическими
format2= 'Название: %s, Цена: %s'
print(format2 % "Гуляш","250")
print(format2 % "Самсы","70")
# Название: Гуляш, Цена: 250
# Название: Самсы, Цена: 70

format3 = 'Название: {}, Цена: {}'
print(format3.format('Шакарап', '35'))
# Название: Шакарап, Цена: 35
#
#
format2= 'Название: %s, Цена: %s'
print (format2 % ("Гуляш","250"), format2 % ("Самсы","70"),sep ='\v')
''' Название: Гуляш, Цена: 250
                          Название: Самсы, Цена: 70
'''


"=============Методы строк ================="
# методы типов данных- функции,к которым мы обращаемся через точку
#dir ( )-показывает какие методы этого класса
'''
    dir(str)----
     '__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

'HELLO'.lower() # 'hello'
'hello'.upper() # 'HELLO'
'Hello'.swapcase() # 'hELLO'
'heLLo'.title() # 'Hello'
'hello world earth'.title()# 'Hello World Earth'
'hello world'.capitalize()#'Hello world'
'hello'.center(11) # '   hello   '
'hello' .center(11, '-') # '---hello---'
'hello' .count('l') # 2
'hello' .count('ll') # 1
'hello hello'.count ('hello') # 2
'hello' .count ('w') # 0
'hello world'.startswith('hell') #True
'hello world'.startswith('H') #False
'hello world' .endswith('ld') #True
'hello world' .find (' ') # 5
'hello world' .find ('o') # 4
'hello world' .find ('wo') # 6
'hello world' .find ('hello') # 0
'hello world' .split () # ['hello','world']
'hello world' .split ('o') # ['hell','w','rld']
'$'.join(['hello','world']) # 'hello$world'
' '.join(['hello','world']) # 'hello world'
''.join(['hello','world']) # 'helloworld'
' '.join(['hello','world'.split()]) # 'hello world'
'o'.join(['hello','world'.split('o')]) # 'hello world
# конкатенация - склеивание строк
'hello'+ 'world' 
chr().isalpha()








"=============== Индексы===================="

# индекс - порядковый номер символа в строке
'h e l l o  w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
srting='hello world'
string [0] # 'h'
string [10] # 'd'
string [5] # ' ' 
 # срез - подстрока строки 
string [0:5] # 'hello'
string [0:6] # 'hello '
string [2:4] # 'll'
string [0:5][2:4] # 'll'


string[:5] # 'hello'
string[6:] # 'world'
string[:] # 'hello world'
string[0:11:2] # 'hlowrd
string[::3] # 'hlwl'
string[::-1] #'dlrow olleh'


#15-task
first, second, third= 1, 2, 3
first=second
third=first
second=third
