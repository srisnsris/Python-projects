#input: Green-red-black-white
#output:Black-Green-red-White

items=[n for n in input("Enter the String").split("-")]  #split will convert string to list
items.sort()       #print(items.sort()) 
 #conevrted into list-->result ; with sotred manner --none result using print; 
 #for that need join to convert after result
print("-".join(items))   # need to change list to str by using join


#how sorted
#l=["green","red","black","white"]
#l.sort()
#print(l)


