from random import randint
import json

class Character(object):
    def __init__(self,name,hp,atk,defence,exp,coin,position,flags):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.exp = exp
        self.coin = coin
        self.x, self.y = position
        self.flags = []
        
    def attack(self,monster):
        if self.atk < monster.defence:
            return '%s was not hurt their defence is too high\n' %(monster.name)
        else:
            monster.hp = monster.hp -(self.atk - monster.defence)
        if monster.hp < 1:
            self.exp = self.exp + monster.exp
            self.coin = self.coin + monster.coin
            if monster.name == 'spider':
                player.flags.append('spider')
            return '%s died and gave %s exp and %s coins.\n' %(monster.name,monster.exp,monster.coin)

        return '%s was attacked for %s HP = %s\n' %(monster.name,(self.atk-monster.defence),monster.hp)

    def run(self,monster):
        chance = randint(1,2)
        if chance == 2:
            return True
        else:
            return '%s was too fast %s could not get away.\n' %(monster.name,self.name)

    def battle(self,monster):
        print self.monster.name + ' has jumped at you\n'

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

class Player(Character):
    
    def __init__(self):
        Character.__init__(self,'Ryan',10,2,2,1,1,Map.getstart(),[])
        
    def __walk__(self, dx, dy):
        x = self.x + dx
        y = self.y + dy
        Mapcall = Map.get(x,y)
        if Mapcall == 'grass' or Mapcall == 'monster':
            self.x += dx
            self.y += dy
        if Mapcall == 'door':
            Map.update(Map.mname)
            print '%s walked through a door and is now in %s.\n' %(player.name,Map.mname)
        if Mapcall == 'wall':
            return 'You walked into a wall.'
        if Mapcall == 'monster':
            self.monster = Monster('Monster')
            player.battle(self.monster)
        if Mapcall == 'boss':
            if Map.mname == 'spiderboss' and not 'spider' in player.flags:
                self.monster = Monster('spider')
                player.battle(self.monster)
            if Map.mname == 'spiderboss' and 'spider' in player.flags:
                self.x += dx
                self.y += dy
                print 'Here lies the dead spiderboss'
        return 'coord(%s, %s)' %(self.x,self.y)

    def walkR(self):
        return self.__walk__(1, 0)

    def walkL(self):
            return self.__walk__(-1,0)

    def walkU(self):
            return self.__walk__(0, 1)

    def walkD(self):
            return self.__walk__(0, -1)

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
        Character.__init__(self,'blob',10,2,2,1,1,(0,0),[])

class Spider(Monster):
    def __init__(self):
        Character.__init__(self,'spider',20,10,5,100,1000,(0,0),[])

class Map():
    def __init__(self):
        self.level = json.load(open('level.json'))
        self.mname = 'map'
        self.data = self.level[self.mname]

    def update(self,mname):
        for x in range(0,len(self.level['doors'])):
            if mname in self.level['doors'][x]:
                if player.x == self.level['doors'][x]['ex'] and player.y == self.level['doors'][x]['ey']:
                    self.data = str(self.level['doors'][x][mname])
                    self.mname = self.data
                    player.x = self.level['doors'][x]['x']
                    player.y = self.level['doors'][x]['y']
                    self.data = self.level[str(self.mname)]

    def get(self,x,y):
        if self.data[y][x] == '-':
            area = randint(0,1)
            if area == 1:
                return 'monster'
            else:
                return 'grass'
        if self.data[y][x] == 'D':
            return 'door'
        if self.data[y][x] == 'W':
            return 'wall'
        if self.data[y][x] == 'B':
            return 'boss'

    def getstart(self):
        start = self.level['start']
        return (start['x'], start['y'])

Map = Map()
player = Player()


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





