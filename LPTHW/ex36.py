from sys import exit

def treasre_room():
    print "You found the treasure room!"
    print "You see the room is glittering with gold everywhere."
    print "What do you do?"

    choice = raw_input("> ")

    if choice == "check for traps":
        print "You found that the room has traps."
        print "You disable the traps and claim the treasure"
        print "You win!"
        exit(0)

    else:
        dead("You step on a trap and die.")


def serpent_room():
    print "As you enter the room, you see a giant serpent."
    print "What do you do?"
    sword = False

    while True:

        choice = raw_input("> ")

        if choice == "look around" and not sword:
            print "you see a sword on the ground. You pick it up."
            sword = True

        elif choice == "attack serpent" and sword == False:
            dead("You bravely charge the serpent but die like a dumbass.")

        elif choice == "attack serpent" and sword == True:
            print "You kill the serpent and see there's another door behind it"
            print "You open the door"
            treasre_room()

        else:
            dead("You make a terrible decision and the serpent attacks you. You die.")

def dead_end():
    print "You enter the room and see nothing in the room."
    print "What do you do?"

    choice = raw_input("> ")

    if choice == "touch wall":
        print "You touch the wall and it starts moving. Towards you. As with the other walls."
        dead("Turns out the walls were design to close in and you die.")

    elif choice == "leave":
        print "You return to the previous room."
        start()

    else:
        print "That doesn't seem like a reasonable choice."
        dead("the door locks behind you and the walls start closing in. You die.")

def dead(reason):
    print reason,"Ayylmao!"
    exit(0)

def start():
    print "You enter a dungeon and see two doors in front of you."
    print "Do you pick the left door or right door?"

    choice = raw_input("> ")

    if choice == "left":
        serpent_room()
    elif choice == "right":
        dead_end()
    else:
        dead("You take too long to survive and starve.")

start()
