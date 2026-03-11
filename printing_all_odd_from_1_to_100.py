# Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

# starting point
number = 0

# the loop to generate odd numbers only
while number <= 100:
    if number % 2 != 0:
        print(number)
    number += 1
