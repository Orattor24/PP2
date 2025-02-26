import os

path = "file_to_delete.txt"

if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File deleted")
else:
    print("File does not exist or cannot be deleted")
