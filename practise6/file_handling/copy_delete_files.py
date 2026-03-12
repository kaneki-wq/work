import shutil
import os

file_path = "sample.txt"

# append new data
with open(file_path, "a") as f:
    f.write("David 28\n")

print("New line appended.")

# copy file
backup_file = "sample_backup.txt"
shutil.copy(file_path, backup_file)
print("Backup created.")

# delete backup safely
if os.path.exists(backup_file):
    os.remove(backup_file)
    print("Backup file deleted.")