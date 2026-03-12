file_path = "sample.txt"

with open(file_path, "w") as f:
    f.write("Alice 25\n")
    f.write("Bob 30\n")
    f.write("Charlie 22\n")

print("File created and data written.")