# imports argv from sys to use
from sys import argv

# sets stores argument values from terminal input to variables script and
# filename
script, filename = argv

# opens textfile from "filename" variable and stores its value into txt variable
txt = open(filename)

# prints a string that mentions your filename
print "Here's your file %r" % filename
# reads the txt variable from earlier and prints its contents
print txt.read()

# prints another string
print "Type the filename again:"
# takes a raw input to be processed further down
file_again = raw_input("> ")


# opens file named in file_again
txt_again = open(file_again)

# prints contents of txt_again after being read
print txt_again.read()
