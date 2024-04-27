punctuation = ",.#@%^&*$"
mystr=input("Enter the string:")

new_str =""
for c in mystr:
    if c not in punctuation:
        new_str+=c
print(new_str)