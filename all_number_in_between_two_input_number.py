# Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

number_1 = int(input("Input first number: "))
number_2 = int(input("Input second number: "))

# used range (start, stop) but add 1 to the start to exclude it
for number in range(number_1 + 1, number_2):
    print(number)
