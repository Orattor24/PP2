lst = []


with open("lst.txt", "r") as file:
    file_content = file.read()[1:-1]
    print(file_content)

    lst = list(map(int, file_content.split(', ')))
print(lst)

