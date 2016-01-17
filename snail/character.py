from actions import Action


class CharacterBase(object):
    def __init__(self, name, hp, attack, defence, experience, coins):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.experience = experience
        self.coins = coins

    def isAlive(self):
        return self.hp > 0

    def __str__(self):
        return "%s: %s" % (self.name, self.hp)

    def fullDescription(self):
        return """
Name......:{name}
Health....:{hp}
Attack....:{attack}
Defence...:{defence}
Experience:{experience}
Coins.....:{coins}""".format(**self.__dict__).lstrip()

# Generates a class sort of like:
# class CharacterBase(object):
#     def __init__(self, name, hp....):
#         self.name = name
#         ....


class Character(CharacterBase):

    def status(self):
        # Maybe do something smarter here later
        return str(self)

    def getBattleAction(self, opponent):
        raise Exception("Unimplemented")

    def getWorldAction(self):
        raise Exception("Unimplemented")


class Monster(Character):

    def getBattleAction(self, other):
        # Monsters just always attack. No brains!
        return Action.Battle.Attack


class Player(Character):
    def __init__(self, position, ioSystem):
        Character.__init__(
            self,
            name="ryan",
            hp=100,
            attack=8,
            defence=2,
            experience=0,
            coins=0)
        self.position = position
        self.io = ioSystem

    def getBattleAction(self, other):
        return self.io.getBattleAction(self, other)

    def getWorldAction(self):
        return self.io.getWorldAction(self)
