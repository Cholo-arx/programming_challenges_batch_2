# 6. Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
# collect 10 input number from the user and appending it into a list
numbers = []

for i in range(1, 11):
    number = float(input(f"input a number {i}: "))
    numbers.append(number)

# staring point
result = numbers[0] - sum(numbers[1:])

print(f"{numbers[0]} - {numbers[1:]} = {result}")
