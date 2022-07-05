# # from base64 import b16decode
# # from calendar import c
# # from re import A
# # from this import d
# " 1- я задача"
# a = int(input("Длина стороны квадрата = ",))
# def qr():
#     per= 4*a
#     print("Периметр =",per)
#     d= ((2)**0.5)*a
#     print("Диагональ =", d)
#     s = a**2
#     print("Площадь =", s)
# # qr()    
" 2-я задача"



#  3-      # 0,3
#  a = 4311
#  b =4321
#  c=5542
#  d= 9871
# a = 9871
# if a//1000>(a//100 - (a//1000)*10) and (a%100)//10>a%10:
#     print('yes')
# else :
#     print('no')


#  4 
sum = 0
for number in range(10000, 100000 ):
    while (number != 0):
        sum = sum + number % 10
        number = number // 10
a = [i for i in range(10000, 100000 ) if i%2==0 and str(i)[2]%2 and sum%4==0]
print(a)

        
#  num = 2005
#  res = str[::-1]
#  print(res)













#  geo_logs = [{'visit2':["Дели", "Индия"]},    # 0,5
#   {"visit3":["Владимир","Россия"]}, 
#  {"visit9":["Курск","Россия"]}]
#  geo_logs = {key:list({(in_v) for in_v in value.items()}) for key,value in geo_logs.items()}
#  print(geo_logs)

#  7ая Задача           # 0,3
# x = input('Х килограм: ')
# a = input('Стоит:')
# kg1 = a / x
# y = input('')
# print(y * kg1)
# print(k*kg1)



# """
# 1) 0,6
# 2) 0,4
# 3) 0,6
# 4) 0,6
# 5) -
# 6) 0,5
# 7) 0,3

# 3 балла

