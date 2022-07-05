"============ Работа с файлами ============"
# open -  функция которая позволяет открыть файл
"============= Режимы================="
# r - read (only for read)
# w - write (только для записи (сначала из файла улаляется , а потом записывается))
# a - append (дозапись( все новое записывается в конец ))
# x - создает файл ,если он уже существует -  ошибка
# rb - чтение в бинарном виде 
# wb - запись в бинарном виде 
# ab - дозапись в бинарном виде 
'когда мы не указываем режим -  по умолчанию чтение'
# open("test.txt") FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

'когда мы открываем файл в режиме w -  он создает пустой файл и потом туда записывает данные'
# open('test.txt', 'w')  - создает пустой файл, если есть такой то очищает и записывает
' когда файла нет - он создает его'
open ('test.txt', 'a')

file = open('test.txt', 'w')
#res = file.read() io.UnsupportedOperation: not readable 
# метод read нельзя использовать при режиме записи и дозаписи
"=============== Write ================"
# file.write('Hello world\n') # в файл записали строку hello world
# file.write('Makers Bootcamp\n')  # после этого продолжает писать строку Makers Bootcamp

# file.writelines(['lin1\n', 'lin2\n', 'lin3\n']) # принимает список со строками и дозаписывает их в файл
# file.close() #  обязательно закрываем файл

# "=============== Read =============="
# file = open ('test.txt') # открываем файл в редиме чтения
# res =  file.read() # считывает весь файл и возвращает строку
# print(file.read(5))  # пустая строка , т.к каретка находится в самом конце файла
# file.seek(0) # каретка переходит в индекс 0 (в начало файла)
# print(file.read(5)) # 'hello' ( считал 5 символов )
# print(file.read(5)) # " worl" ( считал следующие 5 символов)
# file.tell() # 10 показывает текущее положение каретки
# file.readlines() # ['d\n', 'Makers Bootcamp\n', 'lin1\n', 'lin2\n', 'lin3\n'] 
# file.seek(0)
# print(file.readlines()) # ['Hello world\n', 'Makers Bootcamp\n', 'lin1\n', 'lin2\n', 'lin3\n']
# file.seek(0)
# print(file.readlines(10)) # ['Hello world\n'] 
# print(file.tell()) #11
# file.close()
"=============== With =============="
# with -  конструкция, которая в начале конструкции вызывает __enter__, а в конце  call __exit__
# class Test:
#     def __enter__(self):
#         print('Начало работы')
#         return self
#     def __exit__(self, *args, **kwargs):
#         print('Конец работы')
#     def hello(self):
#         print('Hello world')

# with Test() as test:
#     test.hello()
# Начало работы
# Hello world
# Конец работы
file1 = open('test.txt', 'w')
file1.write('hello')
file1.close()
file2 = open('test.txt', 'w')
file2.write('world')
file2.close()
# file1.write('fsdfsfd') # ValueError: I/O operation on closed file.
# потому что file1 мы закрыли

file = open('test.txt', 'w')
file.write('Hello world\nMakers\nBootcamp')
file.seek(0)
file.write('New lines') #New linesld
                        #Makers
                        #Bootcamp

file = open('test.txt', 'w+')
file.write('Hello world\nMakers\nBootcamp')
file.seek(0)
res = file.read()
file.seek(0)
file.write('New lines\n')
file.write(res)
file.close()
print(file.closed) # True
# New lines
# Hello world
# Makers
# Bootcamp

with open('test.txt') as file:
    print(file.read())
    print(file.closed) # False
print(file.closed) # True

string = 123456789
print(int("".join(map(lambda x: x+x, list(str(string))))))
112233445566778899
