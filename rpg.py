from random import randint

class Character(object):
    def __init__(self,name,hp,atk,defence,exp,coin):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.exp = exp
        self.coin = coin
        
    def attack(self,monster):
        if self.atk < monster.defence:
            return '%s was not hurt their defence is too high' %(monster.name)
        else:
            monster.hp = monster.hp -(self.atk - monster.defence)
        if monster.hp < 1:
            self.exp = self.exp + monster.exp
            self.coin = self.coin + monster.coin
            return '%s died and gave %s exp and %s coins.' %(monster.name,monster.exp,monster.coin)
        return '%s was attacked for %s HP = %s' %(monster.name,(self.atk-monster.defence),monster.hp)

    def run(self,monster):
        chance = randint(1,2)
        if chance%2 == 0:
            return '%s ran sucessfully.' %(self.name)
        else:
            return '%s was too fast %s could not get away.' %(monster.name,self.name)
        
class Monster(Character):
    def __init__(self):
        Character.__init__(self,'Monster',10,2,2,0,0)
        self.key = 'penis'
        
player = Character('Ryan',100,10,4,0,0)
monster = Monster()
        

    
