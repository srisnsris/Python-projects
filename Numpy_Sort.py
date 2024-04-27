import numpy as np
a=np.array([50,40,10,20,30])
print(a)

print(np.sort(a))

print(np.sort(a, axis=0))

#print(np.sort(a, axis=1)) axis 1 wont work for 1 dmesnion

b=np.array([[30,50,10],[20,40,60]])
print(np.sort(b))            #default axis=1

print(np.sort(b,axis=0))


d=np.dtype([('name','S10'),('perc',float)])
stud=np.array([("abc",90.3),("def",95.3),("ghi",65.3)],dtype=d)
print(stud)

print(np.sort(stud,order="perc"))

print(np.sort(stud,order="name"))


