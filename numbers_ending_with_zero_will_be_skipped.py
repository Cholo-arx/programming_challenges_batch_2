# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
# %10 - when a number divided with 10 having a ramainder 0 will be skipped
for i in range(0, 101):
    if i % 10 != 0:
        print(i)
