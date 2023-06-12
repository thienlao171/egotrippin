
'''import random
class tank:
    def __init__(self, model, armor,min_damage,max_damage,health):
        self.model=model
        self.armor=armor
        self.damage=random.randint(min_damage, max_damage)
        self.health = health
    def print_info(self):
        print(f'{self.model} имеет любую броню {self.armor} при мм {self.health} при единицах здоровья и уроне {self.damage} в единиц')
    def health_down(self, enemy_damage):
        self.health=enemy_damage
        print(f'{self.model} Броня пробита')
    def shot(self, enemy):
        if enemy.health <=0 or self.damage >= self.health:
            print(f'Экипаж танка {enemy.model} уничтожен')
        else:
            enemy.health_down(enemy.damage)
            print(f'Точное попадание в цель, у противника {enemy.model} осталось {enemy.health} здоровья ')

class Supertank(tank):
    def __init__(self, model, armor,min_damage,max_damage,health):
        super().__init__(model, armor,min_damage,max_damage,health)

tank1=tank('T-34', 90, 20, 30, 100)
tank2=tank('T-90',120, 10, 50, 150)
tank1.print_info()
tank2.print_info()

class user:

tank1.shot(tank2)'''



'vk1.a.Pc4-xQB-VNFHb503SFdIJMwK3uiYcI3luY0HJ9o2pTrRAKfquzvBfGzmaIxFkGyowK66puTh6XKtZUl3P_\
hwXixrsr2XluSiRjCNKC-AAkE0nZ9s5NV3ZQ_v_\
eKsGcPWDUMBM_J3Uuj5Xa8_vCHmhJBVdeSb3mDDumhZ4ffdNEBkAySSXluVWKLyRfXH3mf1pvFGsJZa7vJTpgDkoc2-kQ'