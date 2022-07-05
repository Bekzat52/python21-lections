"================= Build-in fuctions================"
"lambda" # анонимная функция 
# lambda параметры : что функция возвращает
add = lambda a, b : a+ b
print(add(4,5)) # 9

"map" # функция, котторая принимает первым аргументом функцию, вторым итерируемый обьект. map возвращает гененатор,в котором, все элементы - результат принимаемой функции, в которую мы передали элемент из последовательности

map_gen = map(int, ["1", "2", "3", "4"])
print (map_gen) # <map object>
print(list(map_gen)) # [1, 2, 3, 4]

res = list(map(lambda a : a+1, [1, 2, 3, 4, 5])) 
print(res) # [2, 3, 4, 5, 6]

"filter" # функция, которая возвращает генератор, принимает функцию и итерируемый обьект. Результат будет последовательность из элементов итерируемого обьекта, которые прошли фильтр (проверку)
list_= ["Эртай", "Оомат", "Арген", "Бекзат", "Даниэл"]
def startswith_vowels(name):
    vowels= 'УЕЁЫАЩЭЯИЮEYOUAI'
    return name.upper().startwith(tuple(vowels))

res = list(filter(startswith_vowels,list_))
print(res) # ["Эртай", "Оомат", "Арген", "Эракйым"]

"==== filter на цикле for========="
list_= ["Эртай", "Оомат", "Арген", "Бекзат", "Даниэл", "Манас", "Эркайым"]
res = []
for name in list_:
    if startswith_vowels(name):
        res.append(name)
print(res)


"reduce" # нужно импортировать из библиотеки functools 
# эта функция принимает функцию и итерируемый обьект и возвращает 1 результат 

from functools import reduce 
list_ = [1,2,3,4,5,6,7,8,9]
def mul(a,b) :
    return a*b 
res =  reduce(mul,list_)
print(res) # 362880

"==== map на цикле for========="
func = lambda a: a+1
# def func(a):
#       return a+1
res = []
for e in [1,2,3,4,5]:
    res.append(func(e))
print(res) # [2,3,4,5,6]

"=============== Reduce на цикле for ================="
list_=[1,2,3,4,5,6,7,8,9]
def mul(a,b):
    return a*b
res = list_[0]
for b in list_[1:]:
    res = mul(res, b)  
print(res)  

"enumerate" # функция, функция которая принимает последовательность. Возвращает генератор, в котором каждый элемент состоящий из числа и элементов из последовательностей
# enumerate  нумериует элементы по дефолту начиная с 0
list_ = ['a', 'b', 'c', 'd']
for i in enumerate(list_):
    print(i)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')

for index,elem in enumerate(list_[1:]):
    print("index-", index, ":" ,"elem-",elem )
# index- 0 : elem- a
# index- 1 : elem- b
# index- 2 : elem- c
# index- 3 : elem- d

for i in enumerate(list_[1:]):
    print(i)
# (0, 'b')
# (1, 'c')
# (2, 'd')

for i in enumerate(list_[1:], 10):
    print(i)
# (10, 'b')
# (11, 'c')
# (12, 'd')

" zip " # соединяет последовательности
list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", 'b', 'c', 'd', 'e', 'f']
print(list(zip(list1, list2)))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f')]
print(dict(zip(list1, list2)))
# {1 : 'a', 2: 'b', 3: 'c', 4:'d', 5:'e', 6:'f' }


list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c"]
print(list(zip(list1, list2)))
# [(1, 'a'), (2, 'b'), (3, 'c')]

list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c", "d", "e", "f"]
list3 = [1.9, 2.7, 3.0, 4.5]
print(list(zip(list1, list2, list3)))
# [(1, 'a', 1.9), (2, 'b', 2.7), (3, 'c', 3.0), (4, 'd', 4.5)]

list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c", "d", "e", "f"]
list3 = [1.9, 2.7, 3.0, 4.5]
list4 = [(1,2), (3,4)]
print(list(zip(list1, list2, list3, list4)))
# [(1, 'a', 1.9, (1, 2)), (2, 'b', 2.7, (3, 4))]