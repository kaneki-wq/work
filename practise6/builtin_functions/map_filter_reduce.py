from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map example
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# filter example
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# reduce example
sum_all = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce:", sum_all)

# other built-in functions
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Length:", len(numbers))