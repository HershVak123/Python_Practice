from sys import argv

script, short = argv

print "You named this script:", script
pet_name = raw_input("your " + short + " is:")

print "So you petname is %r" % (pet_name)
