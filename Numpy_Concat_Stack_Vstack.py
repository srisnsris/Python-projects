import numpy as np
a=np.arange(6).reshape(2,3)  #two rows 3 column
print(a)

b=np.arange(7,13).reshape(2,3)  
print(b)

print(np.concatenate((a,b)))

print(np.concatenate((a,b),axis=1))  #first row a, and b conc
print(np.concatenate((a,b),axis=0))


print(np.stack((a,b))) #conc merge all ;stack as two dimens


print(np.stack((a,b),axis=1))

print(np.vstack((a,b)))
print(np.hstack((a,b)))  #similar to conc rows axis



print(np.dstack((a,b)))



