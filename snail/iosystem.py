from userInput import promptUser
from actions import Action

class BaseIOSystem(object):
    """This provides the user input/output endpoints."""

    def attackMissed(self, attacker, defender):
        raise Exception("unimplemented")

    def attackHit(self, attacker, defender, damage):
        raise Exception("unimplemented")

    def runSuccess(self, attacker, defender):
        raise Exception("unimplemented")

    def runFailed(self, attacker, defender):
        raise Exception("unimplemented")

    def getBattleAction(self, player, other):
        raise Exception("unimplemented")

    def getWorldAction(self, player):
        raise Exception("unimplemented")

    def enteredLocation(self, pos):
        raise Exception("unimplemented")

    def teleported(self, pos):
        raise Exception("unimplemented")

class ConsoleIOSystem:
    """Prompt the user via raw_input and show output via print"""
    # Handlers for various actions in the game
    def attackMissed(self, attacker, defender):
        print "Attack missed"

    def attackHit(self, attacker, defender, damage):
        print "Attack hit for %s damage" % damage

    def runSuccess(self, attacker, defender):
        print "%s successfully ran" % attacker

    def runFailed(self, attacker, defender):
        print "%s wasn't fast enough to run" % attacker

    def enteredLocation(self, pos):
        print "Moved"

    def teleported(self, pos):
        print "Teleported to ", pos

    # Handlers for getting inputs from the user in the game
    def getBattleAction(self, player, other):
        while True:
            action = self.promptUser(
                "You're in a battle what would you like to do",
                ["attack", "run", "status"])

            if action == "status":
                print "You:", player.status()
                print "Them:", other.status()
                continue # Ask again since 'status' isn't an action.

            if action == "run":
                return Action.Battle.Run

            if action == "attack":
                return Action.Battle.Attack

            # We shouldn't make it down here, but if we do somehow...
            print "Invalid action '%s'" % action

    def getWorldAction(self, player):
        options = ["up", "down", "left", "right", "help", "status"]
        while True:
            action = self.promptUser(
                "You're at %s" % player.position, options)

            if action == "help":
                print "up/down/left/right - Move your character"
                print "status - view your character"
                print "help - show this again"
            elif action == "status":
                print player.status()
            else:
                return {
                    "up": Action.Move.Up,
                    "down": Action.Move.Down,
                    "left": Action.Move.Left,
                    "right": Action.Move.Right
                }[action]


    def promptUser(self, prompt, options):
        while True:
            userInput = raw_input(prompt+"\n>")

            if userInput in options:
                return userInput
            else:
                print "Invalid option. Available actions:"
                print options
