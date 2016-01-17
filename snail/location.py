from actions import Action
class Location(object):
    def __init__(self, room="", x=0, y=0):
        self.room = room
        self.x = x
        self.y = y

    def copy(self):
        return Location(self.room, self.x, self.y)

    def move(self, direction):
        delta = { # dx, dy
            Action.Move.Up:(0,-1),
            Action.Move.Down:(0,1),
            Action.Move.Left:(-1,0),
            Action.Move.Right:(1,0)
        }[direction]
        self.x += delta[0]
        self.y += delta[1]

    def __str__(self):
        return "Room:%s <%s, %s>" % (self.room, self.x, self.y)

