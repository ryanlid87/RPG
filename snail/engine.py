from world import Level
from character import Player
from actions import Action

class Engine:
    def __init__(self, ioSystem):
        self.ioSystem = ioSystem
        self.loadLevel("1")

    def loadLevel(self, level):
        self.level = Level(level)
        self.player = Player(self.level.spawnLocation, self.ioSystem)

    def battle(self, attacker, defender):
        """Perform a battle"""
        while attacker.isAlive():
            action = attacker.getBattleAction(defender)
            if action == Action.Battle.Attack:
                damage = attacker.attack - defender.defence
                if damage <= 0: # Defence > attack
                    self.ioSystem.attackMissed(attacker, defender)
                else:
                    self.ioSystem.attackHit(attacker, defender, damage)
                    defender.hp -= damage
            elif action == Action.Battle.Run:
                if chance(.50):
                    self.ioSystem.runSuccess(attacker, defender)
                    return
                else:
                    self.ioSystem.runFailed(attacker, defender)
            else:
                raise Exception("Invalid battle action: %s" %action)

            attacker, defender = defender, attacker

    def move(self, player, direction):
        """Move the player in [direction]."""
        position = player.position

        # Get a copy of the players position and move it to the destination
        nextPosition = position.copy()
        nextPosition.move(direction)

        nextTile = self.level.at(nextPosition)
        if nextTile.canEnter(player):
            player.position = nextPosition
            nextTile.onEnter(player, self)
            self.ioSystem.enteredLocation(nextPosition)

    def replaceTile(self, location, tile):
        self.level.setTile(location, tile)

    def teleport(self,  player, position):
        self.player.position = position
        self.ioSystem.teleported(position)

    def run(self):
        while True:
            action = self.ioSystem.getWorldAction(self.player)
            self.move(self.player, action)
