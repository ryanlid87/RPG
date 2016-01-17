import character
from location import Location

"""Each spot in a map has a corrosponding Tile object that
lets the game know if the player can enter that tile.

For example they can't enter a wall, they can enter a grass
area. This also supports something like "They can only enter
this door if they have a key."

if newTile.canEnter(player):
    newTile.onEnter(player)

"""

classes = {}


class Tile(object):
    def canEnter(self, player):
        """Returns True/False for if the player can enter this cell as is."""
        raise Exception("Unimplemented")

    def onEnter(self, player, engine):
        """The player has entered this cell, perform any actions."""
        pass


class Grass(Tile):
    def canEnter(self, player):
        return True
classes["Grass"] = Grass


class Wall(Tile):
    def canEnter(self, player):
        return False
classes["Wall"] = Wall


class Monster(Tile):
    def __init__(self, args=None):
        if args is None:
            args = {
                "name": "Monster",
                "hp": 10,
                "attack": 2,
                "defence": 2,
                "experience": 1,
                "coins": 1
            }

        self.monster = character.Monster(**args)

    def canEnter(self, player):
        return True

    def onEnter(self, player, engine):
        engine.battle(player, self.monster)
        engine.replaceTile(player.position, Grass())
        return True
classes["Monster"] = Monster


class Door(Tile):
    def __init__(self, doorArgs):
        self.location = Location(doorArgs["room"],
                                 doorArgs["exit"]["x"],
                                 doorArgs["exit"]["y"])

    def canEnter(self, player):
        # would make sense to check the destination
        # but whatever, assume it's unblocked
        return True

    def onEnter(self, player, engine):
        engine.teleport(player, self.location)
classes["Door"] = Door


class Chest(Tile):
    """ Chests don't work right yet..."""
    def __init__(self, contents):
        pass

    def canEnter(self, player):
        return True

    def onEnter(self, player, engine):
        pass
classes["Chest"] = Chest

# Others:
# Item - item drops/things to pick up there
# Trap - dammage the player
# LockedDoor - a door that can only be entered with the right key
# Lever
#
# Also explore having tiles provide extra actions
