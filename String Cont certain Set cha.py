import re

def is_allowed(string):
    chare=re.compile(r'[^a-zA-Z0-9]')
    string=chare.search(string)
    return not bool(string)
print(is_allowed("123Abcs1234"))
print(is_allowed("@#$"))