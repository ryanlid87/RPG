import tiles
import json
from location import Location

"""A level consists of a spawn point, and one or more
rooms.

Each room has a map and a legend that goes with it.
"""


class Legend(object):
    def __init__(self, legendData):
        self.legend = legendData

    def create(self, mapChar):
        tileSpec = self.legend[mapChar]
        classObj = tiles.classes[tileSpec["type"]]
        if "args" in tileSpec:
            instance = classObj(tileSpec["args"])
        else:
            instance = classObj()
        return instance


class Room(object):
    def __init__(self, data):
        legend = Legend(data["legend"])

        self.tiles = []
        for mapRow in data["map"]:
            tileRow = []
            self.tiles.append(tileRow)

            for cell in mapRow:
                tileRow.append(legend.create(cell))

    def at(self, x, y):
        return self.tiles[y][x]

    def setTile(self, x, y, tile):
        self.tiles[y][x] = tile


class Level(object):
    def __init__(self, levelName):
        data = json.load(file("levels/%s.json" % levelName))
        self.spawnLocation = Location()
        self.rooms = {}

        for key, value in data.items():
            if key == "spawn":
                self.spawnLocation.room = value["room"]
                at = value["at"]
                self.spawnLocation.x = at["x"]
                self.spawnLocation.y = at["y"]
            else:
                self.rooms[key] = Room(value)

    def setTile(self, location, tile):
        self.rooms[location.room].setTile(location.x, location.y, tile)

    def at(self, location):
        return self.rooms[location.room].at(location.x, location.y)
