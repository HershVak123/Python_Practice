# assigns number of available cars
cars = 100
# describes the amount of available spots in a car
space_in_a_car = 4.0
# assigns the number of available drivers
drivers = 30
# assigns the number of passengers
passengers = 90
# assigns the number of not driven cars as the total number of available cars minus the number of drivers
cars_not_driven = cars - drivers
# assigns the number of cars driven as equal to the number of drivers
cars_driven = drivers
# assigns the carpool capacity as the number of cars driven times the number of available spots per car
carpool_capacity = cars_driven * space_in_a_car
# assigns the avg number of people needed to be in each car calculated as number of passengers divided by the number of cars driven.
average_passengers_per_car = passengers / cars_driven


print "Thers are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
