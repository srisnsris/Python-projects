import numpy as np
a=np.arange(10,100,10)
print(a)
print(np.where(a==40))  #will display index values
a=np.array([10,20,30,40,0,60,10,10])
print(a)
print(np.where(a==10))

print(np.where(a%20==0))


b=np.arange(10,100,10)
print(b)
print(np.searchsorted(b,45)) #will display where to insert
#binar search;return the index where valu where value should be inserted
#noy insetin values

print(np.searchsorted(b,[15,25,35]))

