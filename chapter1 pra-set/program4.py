import os

# Specify the directory path
path = "chapter1" 

# Get the list of files and folders
contents = os.listdir(path)

# Print each item
for item in contents:
    print(item)