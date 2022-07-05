
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

