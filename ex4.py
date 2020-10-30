cars = 100
# Changing space_in_a_car to 4 from 4.0 yields carpool capacity as 120, instead of 120.0
space_in_a_car = 4
drivers = 30
# Doesn't say whether passengers include drivers or not. The assumption seems to be that passengers include drivers. Or this could be included in the assumption for space_in_a_caras 4
passengers = 91
cars_not_driven = cars - drivers
cars_driven = drivers
# The author's error screenshot, and my own addition of comments, seem to have shaken up the meaning of line numbers 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Adding a space inside the double quotes adds a redundant space character
print("There are ", cars, "cars available.")
print("There are only ", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
# Not adding spaces after the commas seems to be okay - this is something probably only done 
print("We have",passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")