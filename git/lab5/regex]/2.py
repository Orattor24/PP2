import re
tr = re.fullmatch(r'a{1}.b{1,3}', "ab")
print(bool(tr))