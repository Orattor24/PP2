source = "example.txt"
destination = "destination.txt"

with open(source, "r", encoding="utf-8") as src, open(destination, "w", encoding="utf-8") as dest:
    dest.write(src.read())
