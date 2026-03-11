# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
# create a list to store 10 numbers
numbers = []
# input using loop
for i in range(1, 11):
    number = float(input(f"Input 10 number to sum it (number {i}): "))
    numbers.append(number)

print(f"The sum of the ten numbers is {sum(numbers)}")
