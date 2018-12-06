#imports argv from sys
from sys import argv

# assigns values to variables from whatever is input in argv
script, input_file = argv

# defines a function
def print_all(f):
    # tells the function to read whatever file is input into the function
    print f.read()

# defines another function
def rewind(f):
    # tells the function to set the "cursor" to return to the 0th position of
    # the doc
    f.seek(0)

# defines another function w/ 2 arguments
def print_a_line(line_count, f):
    # prints an integer reads whatever line the cursor is on in the doc
    print line_count, f.readline()

# opens the input file from argv and assigns it to a variable
current_file = open(input_file)

# prints a string with a line break
print "First let's print the whole file:\n"

# calls our function to read and print the whole document
print_all(current_file)

# prints a string
print "Now let's rewind, kind of like a tape."

# calls our function to return the cursor to the start of the doc
rewind(current_file)

# prints a string
print "Let's print three lines:"

# assigns a value to keep track of the line we are on in our document
current_line = 1
#calls our function to print line # and contents of that line
print_a_line(current_line, current_file)

# increments line counter by 1
current_line += 1
# calls function to print line count and second line contents
print_a_line(current_line, current_file)

# increments line count by 1
current_line += 1
# prints line count and contents of that line
print_a_line(current_line, current_file)
