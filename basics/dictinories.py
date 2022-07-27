"==================Словари==================="
#словарь (dict) - изменяемый ,итерируемый,неиндексируемый, неупорядоченный тип данных ,в которых значиения хранятся в парах (ключ: значение)

dict_={"a":"hello", "b":2, "c":3}
print(dict_["a"]) #hello

print (locals())

# ключами в словаре могут являться  только неизменяемые типы данных
# значениями с вловаре могут являться любые типы данных
# ключи должны быть уникальными
dict_={1:"hello",
"a":4,
4.5:{"a":5},
# { "s":4}:44 #TypeError : unhahsible type: 'dict_'
}
print(dict_[4.5]) #{"a":5}


"=============Создание словарей================"
dict1 = {"a":3}
dict2 = dict( [ ('key1', 'value1'), ('key2', 'value2') ] )
# dict2 = {'key1':'value1', 'key2':'value2'}
dict3 = dict( ( ['key1', 'value1'], ('key2', 'value2') ) )
# dict3 = {'key1':'value1', 'key2':'value2'}
dict4 = dict(['ab', 'cd', 'de'])
# dict4 = {"a":"b", 'c':'d', 'd':'e'}
key1, value1 = 'ab'
dict4[key1] = value1
key2, value2 = 'cd'
dict4[key2] = value2
key3, value3 = 'de'
dict4[key3] = value3
dict1.update()

dict5 = dict(['abc']) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
key1, value1 = 'abc' #
dict5[key1] = value1


"=======================Методы словаря============"

#dict_[key]  -достает значение по индексу если нет такого ключа выводит KeyError
# dict_.get(key) - достает значение по индексу ,если нет такого ключа выводит None
# d.keys() # достает все ключи
# d.values()# выводит все значения 
#d.items()# выводит все ключи и значения
dict_.clear()
print(dict_) # {}
dict_= dict.fromkeys([1,2,4])
print(dict_) # {1:None, 2:None,3:None}

dict_=dict.fromkeys([1,2,4],"hello")
print(dict_)  #{1: "hello", 2:"hello", 3:"hello"}

dict_={"a":1, "b":2}
dict_["a"] # 1
dict_["c"] # KeyError
dict_.get("a") # 1
dict_.get("c") # None
dict_.get("c", 5) # 5
dict_.get("a",5) # 1

dict_.keys() # dict_keys([('a', 1 ), ('b', 2)])
dict_.values() # dict_values([1,2])
dict_.items() # dict_items([('a', 1), ('b', 2)])

dict1 = {1:"a", 2:"b", 3:"c"}
dict2 = {3:"d", 4:"e"}
#метод update добавляет пары из второго словаря в первый
dict1.update(dict2)
print(dict1) # {1:"a", 2:"b",3:"d", 4:"e"}
print(dict2) # {3:"d", 4:"e"}
# метод рор удаляет пару по ключу и возвращает значение
popped= dict1.pop(3)
dict1.pop("не существующий ключ") # KeyError

print (dict1) # {1:"a", 2:"b", 4:"e"}
print(popped) # d
# метод popitem удаляет и возвращает последнюю пару 
print(dict1.popitem()) 





