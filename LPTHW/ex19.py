# defines a function and the arguments it takes.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# prints a text string and the value put in an argument
    print "You have %d cheeses!" % cheese_count
# prints a text string and the value assigned to an argument
    print "You have %d boxes of crackers!" % boxes_of_crackers
# prints a string
    print "Man that's enough for a party!"
# prints a string
    print "Get a blanket.\n"


# prints a string
print "We can just give the function numbers directly:"
# calls the function cheese_and_crackers with specified arguments
cheese_and_crackers(20,30)


# prints a string
print "OR, we can use variables from our script:"
# assigns an integer value to variable
amount_of_cheese = 10
# assigns integer value to variable
amount_of_crackers = 50

# calls our function with our earlier assigned variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# prints a string
print "We can even do math inside too:"
# calls our function with math operations as our argument values
cheese_and_crackers(10 + 20, 5 + 6)

# prints a string
print "And we can combine the two, variables and math:"
# calls our function with math operations consisting of our variables and
# integers as our arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
