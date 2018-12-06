print "Enter filename here:"
filename = raw_input("> ")

txt = open(filename)

print "Here's your file %r" % filename
print txt.read()
