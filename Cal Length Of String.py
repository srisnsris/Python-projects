t = "Srinivas Vuppla"
#print(len(t))
def string_length(str1):   #using function
    count=0
    for char in str1:
        count+=1   #count = count+1
    return count
print(string_length(t))