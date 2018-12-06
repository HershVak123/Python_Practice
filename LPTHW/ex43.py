from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement  enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the meutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow up the ship after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the cntral corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate-filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if "shoot" in action:
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your laser hits his costume but misses him entirely."
            print "The Gothon shoots you and kills you"
            return 'death'

        elif "dodge" in action:
            print "You dodge, but then hit a wall."
            print "The Gothon laughs at you and proceeds to shoot you."
            print "You are dead."
            return 'death'

        elif action == "tell a joke":
            print "You tell a joke that the Gothon finds funny."
            print "He breaks down into hysterical laughter."
            print "You take the opportunity to shoot and kill him"
            print "Moving past the Gothon's body, you enter the Weapon Armory"
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE"
            return 'central_corridor'



class LaserWeaponArmory(Scene):

    def enter(self):
        print "As you enter the Armory, you see the neutron bomb"
        print "It is locked in a container that requires a 3 digit code"
        print "You recall that the first two digits are 5 and 4, but you can't"
        print "seem to recall the third digit, so you decide to brute force it"
        print "Unfortunately, if you guerss wrong 10 times the room will shut"
        print "and the defense systems will kill you"
        code = 545
        guess = raw_input("[keypad]> ")
        guesses = 0

        while int(guess) != code and guesses < 10:
            print "BZZD! Wrong!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if int(guess) == code:
            print "You correctly guess the code. The container unlocks and you grab"
            print "the bomb."
            print "You make your way to the bridge to place it."
            return 'the_bridge'
        else:
            print "You use up your last guess and the room locks from the outside."
            print "Auto-turrets deploy in the room and shoot you full of bullets."
            print "You have died"
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print "You enter the bridge and see a group of Gothons tryign to take"
        print "control of it."
        print "They turn and see that you have the neutron bomb."
        print "As a result, they don't draw their weapons out of fear of setting"
        print "the bomb off."

        action = raw_input("> ")

        if "throw bomb" in action:
            print "You throw the bomb at the gothons in a last-resort effort"
            print "to defeat the Gothons."
            print "After your self-sacrificial act, the bomb goes off and blows"
            print "up the ship and everyone on it."
            print "You have died"
            return 'death'

        elif action == "slowly place bomb":
            print "You point your blaster at the Gothons to threaten them."
            print "Being intimidated, they raise their hands in the air"
            print "You place the bomb and set it to explode."
            print "You then back away slowly, makign sure to keep your blaster"
            print "pointed at the bomb."
            print "After making your way to the door, you quickly close it"
            print "And blast the lock to prevent escape"
            print "You start sprinting towards the escape pods"
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"



class EscapePod(Scene):

    def enter(self):
        print "You enter the part of the ship with the escape pods in it."
        print "The area looks heavily damaged, and it looks like only one of"
        print "the 5 pods might be functional."
        print "You decide to take a chance and see which one still works."
        print "Which do you choose?"

        good_pod = 3
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You enter a pod and start it up."
            print "It immediately fails and explodes."
            print "You are dead."
            return 'death'

        else:
            print "You jump into pod %s and hit the button." % guess
            print "It starts up and evacuates from the ship."
            print "You found the right pod!"
            print "As you look out the window, you see the ship explode with"
            print "all the Gothons on it."
            print "You've succeeded in your final mission!"

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job!"
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val


    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
