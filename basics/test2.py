# import random
# a = input('Ваше имя :',)
# b = input("Хотите играть? -",)
# t = 1
# c = random.randint(3, 5)
# print(c)
# while str(b) == 'нет': 
#     break
# d = (input('Угадайте число:', ))
# if int(d)== c:
#     print(f'ВЫ УГАДАЛИ ЧИСЛО!\nКОЛИЧЕСТВО ПОПЫТОК : {t} ')     
# while int(d) != c :
#         v =input('Попробуйте заново:',)
#         t =t+1
# if int(v) ==c :
#             print(f'ВЫ УГАДАЛИ ЧИСЛО!\nКОЛИЧЕСТВО ПОПЫТОК : {t} ')

import datetime
now = datetime.datetime.now()

print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))