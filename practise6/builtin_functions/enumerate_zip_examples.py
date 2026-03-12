names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate example
print("Enumerate:")
for index, name in enumerate(names):
    print(index, name)

# zip example
print("\nZip:")
for name, score in zip(names, scores):
    print(name, score)

# sorted example
numbers = [5, 2, 8, 1]
print("\nSorted:", sorted(numbers))

# type conversion
x = "10"
y = int(x)

print("\nType conversion:")
print(type(x))
print(type(y))