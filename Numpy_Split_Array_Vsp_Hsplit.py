import numpy as np
a=np.arange(10)
print(a)

print(np.split(a,2))   #equal div

#print(np.split(a,3))  #won't split unequal

print(np.array_split(a,2)) 
print(np.array_split(a,3))  #if unequal div,start adjust from last elemts
print(np.array_split(a,4))

print(np.hsplit(a,2))   #horiz spli
b=np.hsplit(a,2)    #can initalize into B

#print(np.vsplit(a,2))  #not work on single dime

c=np.arange(6).reshape(2,3)
print(c)
print(np.vsplit(c,2))

d= (np.vsplit(c,2))
print(d)      #can intalie into other var

#print(np.vsplit(c,3))  #uneqal div

print(np.array_vsplit(c,3)) 