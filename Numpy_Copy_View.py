import numpy as np
a=np.array(['40','20','50','90','30','40'])
print(a)
print(a.dtype)

c=a.copy()
print("COPY=",c)
c[1]=50                   #copied data without changing original data --COPY
print("a=",a,"c=",c)        #   40,50,50,90,30,40


v=a.view()
print("VIEW=",v)
v[1]=11                   #VIEW--referbnce of origina l copy
a[2]=12
print("a=",a,"v=",v)

print("C=",c.base)
print("V=",v.base)


a=np.array(['40','20','50','90','30','40'],dtype="int")
print(a)
print(a.dtype)


a=np.array([10,20,30])
print(a)
print(a.dtype)


a=np.array(['40','20','50','90','30','40'],dtype="int")  #error if we sinsert 'a'
print(a)
print(a.dtype)

d=np.array(['40','20','50','90','30','40','0'])
print(d)
print(d.dtype)
e=d.astype("bool")
print(e)
print(e.dtype)

#view
f=np.array(['40','20','50','90','30','40'])
print(f)
print(f.dtype)


v=f.view()
print("VIEW=",v)
v[1]=11                   #VIEW--referbnce of origina l copy
f[2]=12
print("f=",f,"v=",v)
print("V=",v.base)





