file_path = "sample.txt"

with open(file_path, "r") as f:
    print("Full file content:")
    print(f.read())

with open(file_path, "r") as f:
    print("Reading line by line:")
    for line in f:
        print(line.strip())