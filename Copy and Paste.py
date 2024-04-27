import pyperclip
 
text = "  Welcome 50"   #50 #copy funct conerts all input  to string
 
pyperclip.copy(text)

text2 = pyperclip.paste()

print(type(text2))

