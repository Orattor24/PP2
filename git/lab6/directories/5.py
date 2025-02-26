data = ["Hello", "World", "Python", "Files"]

with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines("\n".join(data))
