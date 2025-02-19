import re
tr = re.fullmatch(r'a.*b', "ab" )
print(bool(tr))