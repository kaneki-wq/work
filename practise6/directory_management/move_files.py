import shutil
import os

source = "sample.txt"
destination = "data/raw/sample.txt"

# move file
if os.path.exists(source):
    shutil.move(source, destination)
    print("File moved to data/raw")

# copy file
shutil.copy(destination, "data/processed/sample_copy.txt")
print("File copied to processed folder")