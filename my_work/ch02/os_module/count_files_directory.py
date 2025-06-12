import os

file_count = 0

for currentdir, dirnames, filenames in os.walk('.'):
    file_count += len(filenames)

print(f"The number of files in the current directory: {file_count}")