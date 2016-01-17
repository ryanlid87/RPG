from iosystem import BaseIOSystem
from actions import Action
from engine import Engine


class EndOfInputException(Exception):
    pass


class TestingIOSystem(BaseIOSystem):
    """An automatic system that moves the player
    through the game and fights all monsters.
    Path is hardcoded to the current level.
    Events seen get recorded in self.events.
    When we run out of preprogrammed actions the
    EndOfInputException is raised.
    """
    def __init__(self):
        self.events = []
        #      room1      the bend    chest
        path = "RRRRRR" + "RRDDLLL" + "D"
        mapping = {
            "R": Action.Move.Right,
            "D": Action.Move.Down,
            "L": Action.Move.Left
        }
        # Convert from string (path) to actual Actions
        self.path = [mapping[action] for action in path]

    def attackMissed(self, attacker, defender):
        self.events.append("attackMissed %s -> %s" % (attacker, defender))

    def attackHit(self, attacker, defender, damage):
        self.events.append("attackHit %s -> %s for %s" %
                           (attacker, defender, damage))

    def runSuccess(self, attacker, defender):
        self.events.append("runSuccess %s -> %s" % (attacker, defender))

    def runFailed(self, attacker, defender):
        self.events.append("runFailed %s -> %s" % (attacker, defender))

    def enteredLocation(self, pos):
        self.events.append("enteredLocation %s" % pos)

    def teleported(self, pos):
        self.events.append("teleported to %s" % pos)

    def getBattleAction(self, player, other):
        return Action.Battle.Attack

    def getWorldAction(self, player):
        if not self.path:
            raise EndOfInputException()

        return self.path.pop(0)

# Now play the game using our testing system for input
ioSystem = TestingIOSystem()
engine = Engine(ioSystem)
try:
    engine.run()
except EndOfInputException:
    # Game is now over, we can check things on the engine
    # and ioSystem to make sure nothing went too wrong.
    print "Game finished:"
    print "-- events --"
    for event in ioSystem.events:
        print event
    print "-- ending stats --"
    print engine.player.fullDescription()
    # We don't actually assert anything, but if we make it here
    # we can at least play though the minimal game and see
    # how the player ended up.
