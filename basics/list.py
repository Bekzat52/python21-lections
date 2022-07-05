"====================List===================="
# списки - изменяемый ,индексируемый,упорядоченный,итерируемыйтип данных,предназначенный для хранения данных в определенном порядке
list_=[1, 3, 40, 'hello', [0.1, 5], {"a":3}]
list_[1] # 2
list_[4] # [0.1, 2]
list_[4][0] # 0.1
list_[-1]["a"] # 3


"===========Создание списков============="
list1 = [1, 2, 3]
list2 = list('hello') # ['h', 'e', 'l', 'l', 'o']
list3 = list(range(1,11)) # [1,2,3,4,5,6,7,8,9,10]
list4 = [1]*5 # [1,1,1,1,1]


"======== Методы списков ============"

list_=[[]]*3
list_[0].append(1)
print(list_) # [[1],[1],[1]]
list_= []
list_.append(1)
print(list_) # [1]
list_.append("hello")
print(list_) # [1, "hello"]
list_.append([1, 2, 3, 4])
print(list_) # [1, "hello", [1, 2, 3, 4]]
list_.append(1, 2, 3) # TypeError : append() takes exactly one argument (3 given)


# clear  очищает список
list_.clear()
print(list_) #[]


# count считатет количество введенного объекта 

lisr_=[1, 2, 4, 3, 1, 4, 5, 7, 1, 1]
list_.count(1) # 4
list_.count(2) # 1
list_.count(4) # 2

list_=['hello', 'hello', 'hello']
list_.count('h') #0
list_.cont('hello') # 3
# len считает количество объектов в списке 
list_=[1, 2, [1, 3, 4, 4], "hello", {"a":4}]
list_.len # 5
# extend добавляет элементы второго списка в первый изменяя первый 
list1=[1, 2, 3]
list2=[4,5,6]
list1.extend(list2)
print(list1) # [1,2,3,4,5,6]
print(list2) # [4,5,6]

#index возвращает первый индекс введенного элемента в списке

list1 = [1, 2, 3, 4, 1, 2, 3, 5, 4, 1]
list_.index(3) # 2
list_.index(1) # 0

# insert добавляет элемент по индексу  list.insert(index.obj)
list_=[1, 2, 3]
list_.insert(0,"hello")
print(list_) # [1, 2, 3, 0, "hello"]
list_.insert(100, "bye")
print(list_) # ["1, 2, 3, 0, "hello", "bye"]

# pop удаляет элемент из списка по индексу + мы его можем сохранить 
list_=[1,2,3,4,5,6,7]
popped=list_.pop()
print(list_, popped) # [1,2,3,4,5,6] 7
popped = list_.pop(1)
print(list_, popped) # [1,3,4,5,6] 2

print([1,2,[3,4,[5,6]]]).pop(2).pop(2).pop(1)  # 6
# remove
list_=[1,2,3,1,2,3,1,2,4,1,2,6]
list_.remove(2)
print(list_) #  [1,3,1,2,3,1,4,1,2,6]
str(list_).replace('2', '').replace(',', '').replace('[', '').replace(']', '').replace(' ', '')


# reverse изменянет список переставляя элементы в обратном порядке
list_=[1,2,3,4,5]
list_.reverse()
print(list_)



#sort сортирует список состоящий из элментов одного типа данных в возрастающем порядке(в алфавитном для строк)
# reverse=True сортирует по убыванию
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort()
print(list_) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_ = ['a', 'c', 'd', 'b', 'f', 'e', 'A', 'C', 'B']
list_.sort()
print(list_) # ['A', 'B', 'C', 'a', 'b', 'c', 'd', 'e', 'f']

list_ = [1,2,3,'hello'] 
list_.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

# reverse=True сортирует по убыванию
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort(reverse=True) # [10,9,8,7,6,5,4,3,2,1]
