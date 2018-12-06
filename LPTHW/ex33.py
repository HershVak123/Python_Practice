def while_loop(input, increment):

    i = 0
    numbers = []

    while i < input:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "

    for num in numbers:
        print num


while_loop(12, 2)
