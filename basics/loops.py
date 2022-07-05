"=============== Циклы ==================="
# циклы- блок кода которая повторяется несколько раз
# while 
# for - цикл которая работает с итерируемыми обьектами .Цикл заканчивает свою работу ,когда он дошел до конца (до последнего элемента ) в итерируемом обьекте
# while -цикл , который работает до тех пор пока условие верное 
from more_itertools import count_cycle


count=10
while count!=0:
    print(count)
    count= count -1
# 10 9 8 7 6 5 4 3 2 1 end
a=0 
while a :
    print("hello")
# не отработает ,так как цикл работает только при булевом значении True .Если условие False условие не будет работать 

for i in range [1,2,3] :
    print (i)
# 1 2 3 

for i in range(5):
    print(i)
# 0 1 2 3 4 

for i in 12345:
    print(i)
# TypeError: 'int' objects is not iterable

num = 12345678
sum = 0
for i in str(num):
    # sum = sum =i 
    # TypeError : unsupported operand type(s) for +: 'int' and 'str'
    sum = sum + int(i)
print (sum) # 36 
string_='hello'

for i in []:
    print (i)
# не отработает вообще ,потому что нет элементов


srting_='hello'
for i in string_:
    print(i)
    string_=string_ + "hello"
    print(string_)
# отработает только 5 раз ,потому что у переменной string_ 


"============= Клбчевые слова в циклах========="
# break - полностью выйти из цикла
# continue - перейти к следующей итерации

for i in range(10):
    if i == 3:
        continue
    print(i)
# 0 1 2 4 5 6 7 8 9

for i in range(10):
    print(i)
    if i == 3:
        continue
# 0 1 2 3 4 5 6 7 8 9

for i in range(10):
    print(i)
    if i == 3:
        break
# 0 1 2 3

for i in range(10):
    if i == 3: break
    print(i)
# 0 1 2

for i in range(10):
    if i < 3: continue
    print(i)
# 3 4 5 6 7 8 9


for i in range(10):
    print(i)
    for j in range(10):
        print(j)
        if j == 5: break
    if i == 2: break

for i in range(1, 11): print(i)
# 1 2 3 4 5 6 7 8 9 10

list_ = [2,1,3,6,2,5,2,8,2]
while 2 in list_:
    list_.remove(2)
print(list_)




"================ Итерирование словарей ==============="
dict_={"a":1, "b":2, "c":3, "d":4}
# при итерации словаря, мы будем получать его ключи
for key in dict_:
    print(key)
# "a" "b" "c" "d"

# при итерации dict_keys, мы получим его ключи
for key in dict_.keys():
    print(key)
# "a" "b" "c" "d"

# при итерации dict_.values , мы будем получать значеня словаря
for value in dict_.values():
    print(value)
# 1 2 3 4 

for key in dict_:
    print (dict_[key])
# так мы тоже выведем щначения 

# при итерации dict_.items , мы будем получать tuple из ключа и значения
for items in dict_.items():
    key =items[0]
    value = items[1]
print(key,value)




# можем распаковать typle на 2 переменные
for key,value in dict_.items():
    print (key,value)

# for key, value in dict1.keys():
# ValueError: not enough values to unpack (expected 2, got 1)
# потому что метод keys возвращает нам только 1 элемент, а мы распаковываем его на 2 переменные


for a, b, c in [ (1,2,3), (4,5,6), (7,8,9) ]:
    print(a, b, c)
# a=1 b=2 c=3 (iter1)
# a=4 b=5 c=6 (iter2)
# a=7 b=8 c=9 (iter3)

for a, b in [(1,2),(2,3),(3,4)]:
    print(a,b)
# a=1 b=2 (iter1)
# a=2 b=3 (iter2)
# a=3 b=4 (iter3)

a=[]
for i in a :
    print ("for")
else : # сработает только если цикл ни разу не стработал
    print('else')

while 0 :
    print("while")
else : # не сработает только если цикл был прерван break
    print ("else")

a = 1
while a:
    print("while") 
    if a == 1:
        break
else:
    # не сработает только если цикл был прерван break
    print("else") 