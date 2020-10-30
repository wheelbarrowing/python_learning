# Printing the intent to count chickens (revised this line to not read Intent Number 1, since someone in the future might put something above this and then this won't be a part of a continuous program. Also interesting, # works across word wrap)
print("I will now count my chickens:")
# (Interesting that the comment for functionality is written above each line. Does this change on projects?) Intent to print calculation of Hens as 25 + (30/6). BODMAS is followed, so no need to put in extra parantheses
print("Hens", 25 + 30 / 6)
# (I don't understand what the % symbol is doing. How is BODMAS followed with %?) Intent to print calculation of Roosters as 100 - 25 * 3 %4. Shouldn't this be 100 - (25*(3%4)). 
#Update 20201030 0859 :PEMDAS is followed - Paranthesis, exponents, multiplication, division, addition, subtraction. Also, learning from here that the priority order is P, E, MD, AS. Which means that if M and D operations occur, the priority is set from left to right. So a D sign to the left of an M sign will yield division first. (https://stackoverflow.com/questions/48937457/how-do-order-of-operations-go-on-python) (More detail here - https://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html)
#Test line here
print("Test 1 for PEMDAS with MD order: ", 4.0 + 8.0*4.0/2.0)
print("Test 2 for PEMDAS with MD order: ", 4.0 + 8.0/4.0*2.0)
print("In Test 2, a pure PEMDAS would have yielded the answer as 5, but a clubbing of MD and L-R priority yields it as 8")
# Evaluating again - 100 - ((25*3) % 4) = 100 - (75%4) = 100 - (72+3)%4 = 100 - 3 = 97
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0) 
# Printing the intent to count the eggs
print("Now I will count the eggs:")
# Printing egg count as a combination of numbers and mathematical operations
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)
# Printing the intent to answer to a strictly less than boolean question
print("Is it true that 3 + 2 < 5 -7?")
# Printing the answer to a strictly less than boolean question
print(3.0 + 2.0 < 5.0 - 7.0)
# Printing a combination to the question
print("What is 3 + 2?", 3.0 + 2.0)
print("What is 5 - 7?", 5.0 - 7.0)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal?", 5.0 >=-2.0)
print("Is it less or equal?", 5.0 <=-2.0)
