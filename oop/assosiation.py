"==================== Ассоциация ===================="
# Ассоциация - принцип ООП, в котором лва класса друг с другом связаны. Делится на 2принципа:
# 1 - агрегация (более слабая связь)
# 2 - композиция (более сильная связь)

class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100

class Iphone:
    def __init__(self, color:str):
        self.color = color
        # когда мы создаем обьект от другого класса прям внутри другого - композиция
        self.battery = Battery()

class Nokia:
    def __init__(self, color:str, battery:Battery):
        self.color = color
        self.battery = battery
        # когда мы принимаем уже созданный вне класса обьект - агрегация


iphone = Iphone('золотой')

del iphone # обьект батарейки удаляется вместе с обьектом  Iphone "композиция"


battery = Battery()
nokia = Nokia('green', battery) # удаялет только обьект  nokia
                                # обьект батарейки сохраняется "агрегация"
                                