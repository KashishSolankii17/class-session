numbers = [10,20,30,40,50]
print(numbers, type(numbers), id(numbers))


# # REFERENCE copy operation
my_numbers = numbers

print(my_numbers, type(my_numbers), id(my_numbers))

numbers[2] = 1122

print(numbers)
print(my_numbers)
