import numpy as np
a=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(a)
print(np.shape(a))
print(np.amin(a))
print(np.amin(a,axis=0))  #axis=0 colum opers
print(np.amin(a,axis=1))  #axis=1 row opers
print(np.amax(a))
print(np.amax(a,axis=0))
print(np.amax(a,axis=1))
print(np.average(a))
print(np.average(a,axis=0))
print(np.average(a,axis=1))
W=[1,2,3]
print(np.average(a,weights=W,axis=0))

b=np.array([[10,20,30],[40,50,60],[70,80,90]])

W=[1,2,3]
print(np.average(b,weights=W,axis=0))  #axis=1

print(np.mean(a))

print(np.mean(a,axis=0))   #axis=0 colum operation,1 rows oper
print(np.median(a,axis=0))
print(np.median(a,axis=1))
print(np.var(a,axis=1))
print(np.var(a))
print(np.std(a,axis=1))
print(np.std(a,axis=0))
print(np.std(a))