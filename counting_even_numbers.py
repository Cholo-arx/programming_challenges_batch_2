# 7.Create a program that ask user to input 10 numbers. Print how many are even numbers.
# create a list to store 10 numbers
numbers = []
# use for loop to store 10 input from the user
for i in range(1, 11):
    number = float(input(f"Input 10 number to sum it (number {i}): "))
    numbers.append(number)

# count the even numbers
even_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count += 1
print(f"there are {even_count} even numbers in the input")
