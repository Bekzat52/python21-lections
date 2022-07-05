from unicodedata import decimal


from decimal import Decimal
x=Decimal(input('Введите первое число:', ))
y=Decimal(input('Введите второе число:', ))
op_=(input('Выберите операцию из следующих +-*/%**// :', ))
if op_.count('+')==1 :
    print(x+y)
elif op_.count('-')==1 :
    print(x-y)
elif op_.count('*')==1 :
    print(x*y)
elif op_.count('/')==1 :
    print(x/y)
elif op_.count('%')==1 :
    print(x%y)
elif op_.count('**')==1 :
    print(x**y)
elif op_.count('//')==1 :
    print(x//y)
else :
    print("Данной операции нет в системе")

