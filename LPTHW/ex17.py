from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file, 'r').read()

print "The input file is %d bytes long" % len(in_file)

out_file = open(to_file, 'w').write(in_file)

print "alirght, copy finished."
