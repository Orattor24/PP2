path = "example.txt"
with open(path, "r", encoding="utf-8") as f:
    print("Number of lines:", sum(1 for _ in f))
