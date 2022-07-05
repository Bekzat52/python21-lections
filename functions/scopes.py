"================== Области видимости и пространства имен================"
locals() # -  возвращает словарь со всеми локальными переменненными
globals() # - возвращает словарь со всеми глобальными  переменненными

# LEGB - local,enclosed,global,build-in
" Built-in " - # встроенное пространство имен (все пространственные переменные(print,input,sum,max,min,len,abs,int,str,dict...))

# Globals - глобальные пространство имен  ( все переменные внутри файла, которые создали мы )

# чтобы узнать ,что находится в глобальном пространстве ,можно испольщовать функцию globals()
" Enclosed " # это прострванство находящееся между двумя пространствами
"Local"  # какое то закрытое пространство
count = 0 
def add():
    global count # 
    print(count)
    count += 1 
add ()
add ()
add () 
print(count)   
# 0 1 2 3 
count = 0 
def add():
    global count
    count += 1
    print(count)
add ()
add ()
add () 
print(count) 
# 1 2 3 3 
a = "global"
def outer_func():
    a= "enclosed"
    
    def inner_func():
        a = 'local'
        print(a)
    print(a)
print(a)
outer_func()    
# global enclosed
a = "global"
def outer_func():
    a= "enclosed"
    
    def inner_func():
        a = 'local'
        print(a)
    print(a)
print(a)
outer_func() 
inner_func() 
#global  enclosed NameError


def count(i) :
    counter= 0

    def add():
        nonlocal counter # доступ на чтение и изменение локальной перемнной counter 
        print(counter)
        counter += 1
    for  _ in range(i):
        add()
count(10)
# 0 1 2 3 4 5 6 7 8 9

sum = 5
def func():
    sum = 10
    def inner_func():
        sum = 20
        def inner2__func():
            sum = 30
            print(sum)
        inner2_func()
    inner_func()
func()

