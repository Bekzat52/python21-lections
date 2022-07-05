import random
words = ['оливье', "дембель", "родина", "телефон", "стол"]
word1 = random.choice(words)
secret_word = "*" * len(word1)
print(word1)

start = input('Начнём игру? - ',)
if 'да'== start or 'ДА'== start or 'Да'== start or 'дА' == start :
    t= len(word1)
    tries = 0
    while t!= tries :
        print(f'Слово - {secret_word}')
        w =input('Ваша буква - ',)
        if w.upper() in word1 or w.lower() in word1:
            tries += 1
            print(f'Количество попыток  {tries}')
            k = ''
            for i in range(t):
                if w == word1[i]:
                    k = k + w
                else:
                    k = k + secret_word[i]
            secret_word = k 
        else:
            print("Данной буквы нет в слове")
            tries += 1
            print(f'Количество попыток  {tries}')
            continue
    if secret_word == word1:
        print(f'Вы угадали слово за {tries} попытки')
    else :
        print('Вы не угадали!')
        print(f'Количество попыток  {tries}')
else :
    print('Не будем играть')
