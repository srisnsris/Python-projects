import re

text='Python Life'
print("Original Text:",text)
print("Without White Spacs:",re.sub(r'\s+', '50', text))  #\s old value replacing with 50 or '' new value