# 4. Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
# ask for input
number_1 = int(input("input the first number: "))
number_2 = int(input("input the second number: "))

# use while loop to re-enter an input if the user typed 0 in number_2
while number_2 == 0:
    print("any number divided by zero is undefined")
    number_2 = int(input("input the second number: "))

# proceed the operation if the while loop is successfully meet
print(
    f"the rounded quotient of {number_1} and {number_2} is {number_1 // number_2}")
