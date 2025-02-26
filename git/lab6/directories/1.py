'''Python Directories and Files exercises
Write a Python program to list only directories, files and all directories, files in a specified path.
Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
Write a Python program to count the number of lines in a text file.
Write a Python program to write a list to a file.
Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
Write a Python program to copy the contents of a file to another file
Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.'''

import os

path = "C:\\Users" 

print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print("All:", os.listdir(path))

