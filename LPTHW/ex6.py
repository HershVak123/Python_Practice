# assigns a string to x that has string formatting
x = "There are %d types of people." % 10
# assigns one word string to binary variable
binary = "binary"
# assigns "don't" to do_not variable
do_not = "don't"
# assigns sentence to y variable that has string formatting
y = "Those who know %s and those who %s." % (binary, do_not)

# prints whatever was assigned to x
print x
# prints whatever was assigned to y
print y

# prints a string that is string-formatted to print x
print "I said: %r." % x
# prints a string that is string-formatted to print y
print "I also said: '%s'." % y

# assigns False boolean value to variable
hilarious = False
# assigns a string w/ string formatting to variable
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the joke_evaluation variable to be string formatted w/ "hilarious" value
print joke_evaluation % hilarious

# assigns a string to w
w = "This is the left side of..."
# assigns a string to e
e = "a string with a right side."

# prints concatinated w and e
print w + e 
