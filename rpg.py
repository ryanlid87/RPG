from random import randint
import json

class Character(object):
    def __init__(self,name,hp,atk,defence,exp,coin,position):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.exp = exp
        self.coin = coin
        self.x, self.y = position

    def attack(self,monster):
        if self.atk < monster.defence:
            return '%s was not hurt their defence is too high\n' %(monster.name)
        else:
            monster.hp = monster.hp -(self.atk - monster.defence)
        if monster.hp < 1:
            self.exp = self.exp + monster.exp
            self.coin = self.coin + monster.coin
            return '%s died and gave %s exp and %s coins.\n' %(monster.name,monster.exp,monster.coin)

        return '%s was attacked for %s HP = %s\n' %(monster.name,(self.atk-monster.defence),monster.hp)

    def run(self,monster):
        chance = randint(1,2)
        if chance == 2:
            return True
        else:
            return '%s was too fast %s could not get away.\n' %(monster.name,self.name)

    def __walk__(self, dx, dy):
        x = self.x + dx
        y = self.y + dy
        Mapcall = Map.get(x,y)
        if Mapcall == 'grass' or Mapcall == 'monster':
            self.x += dx
            self.y += dy
        if Mapcall == 'door':
            Map.update(Map.mname)
            print 'you entered a new room' # just for now
        if Mapcall == 'wall':
            return 'You walked into a wall.'
        if Mapcall == 'monster':
            self.monster = Monster()
            player.battle(self.monster)
        return 'coord(%s, %s)' %(self.x,self.y)

    def walkR(self):
        return self.__walk__(1, 0)

    def walkL(self):
            return self.__walk__(-1,0)

    def walkU(self):
            return self.__walk__(0, 1)

    def walkD(self):
            return self.__walk__(0, -1)

    def battle(self,monster):
        print 'a monster has jumped at you\n'

        while self.monster:
            decide = raw_input('what do you do? (attack or run)?')
            if decide == 'attack':
                print self.attack(monster)
                if self.monster.hp < 1:
                    self.monster = None
                else:
                    print monster.attack(player)
            if decide == 'run':
                runattempt = self.run(monster)
                if runattempt == True:
                    print '%s ran sucessfully.\n' %(self.name)
                    self.monster = None
                else:
                    print runattempt
                    print monster.attack(player)
    def status(self):
        return 'hp = %s, atk = %s, def = %s, exp = %s, coins = %s' %(player.hp,player.atk,player.defence,player.exp,player.coin)
    def help(self):
        return ''' Here are the controls for the game:
        up - moves character up one pixel
        down - moves character down one pixel
        left - moves character left one pixel
        right - moves character right one pixel
        status - shows status of character
                '''

class Monster(Character):
    def __init__(self):
        Character.__init__(self,'Monster',10,2,2,1,1,(0,0))
        #equip has name of weapon, atk value
        self.equip = ['Rubber Sword',1]
        self.atk = self.atk + self.equip[1]

class Map():
    def __init__(self):
        self.level = json.load(open('level.json'))
        self.mname = 'map'
        self.data = self.level[self.mname]

    def update(self,mname):
        self.data = self.level['doors'][0][mname]
        Map.mname = self.data
        player.x = self.data['x']
        player.y = self.data['y']

    def get(self,x,y):
        try:
            if self.data[x][y] == '-':
                area = randint(0,1)
                if area == 1:
                    return 'monster'
                else:
                    return 'grass'
            if self.data[x][y] == 'D':
                return 'door'
            if self.data[x][y] == 'W':
                return 'wall'
        except:
            return 'wall'

    def getstart(self):
        start = self.level['start']
        return (start['x'], start['y'])

Map = Map()
player = Character('Ryan',100,10,4,0,0, Map.getstart())


Commands = {
    'up': player.walkU,
    'down': player.walkD,
    'left': player.walkL,
    'right': player.walkR,
    'status': player.status,
    'help': player.help,
    }

while(player.hp > 0):
    line = raw_input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                print Commands[c]()
                commandFound = True
                break
        if not commandFound:
            print "%s doesn't understand the suggestion." % player.name





