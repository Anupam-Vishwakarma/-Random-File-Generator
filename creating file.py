import random
import string
import os

# Define the directory where you want to create the files
directory = 'C:/Users/Anupam/OneDrive/Documents/pyfolder'

# Define the number of files you want to create
num_files = 100

# Define the file extension
file_extension = '.txt'

# Create a list of random file names
file_names = [''.join(random.choices(string.ascii_lowercase, k=8)) + file_extension for _ in range(num_files)]
#string.ascii_lowercase -->give a lowercase character
#random.choice--> gives a single character 8 times(k)
#join-->join the characters gathered by random.choicew with seperartion''(in this case)
#range-->range of the number of files to be created
#file_names-->list of file names

 
# Create the files
#
for file_name in file_names:
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as f:
        pass  # You can add some content to the file if you want

print(f"Created {num_files} files with random names:")
for file_name in file_names:
    print(file_name)