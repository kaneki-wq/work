import os

# create nested directories
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

print("Directories created.")

# list files and folders
print("Contents of current directory:")
print(os.listdir())

# current directory
print("Current path:", os.getcwd())