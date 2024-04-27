import numpy as np
a=np.arange(0,10,3,dtype="int")   #step siz 2,3,..
print(a)

a=np.arange(0,10,3,dtype="float")   #10 will not be inclde
print(a)

a1=np.linspace(0,10,5)  #10 will be included
print(a1)


a1=np.linspace(0,10,5,endpoint=False)    #false;10 not inclded
print(a1)


a1=np.linspace(0,10,5,endpoint=False,retstep=True)    #re step diff size 2
print(a1)


a1=np.linspace(0,10,endpoint=False)    #removed stepsize,ret step ;which default step size is 50
print(a1)


a1=np.linspace(0,10,endpoint=False,dtype="int")    #dtype=int,float
print(a1)

a1=np.linspace(0,10,endpoint=False,dtype="float")    #dtype=int,float
print(a1)

a1=np.linspace(0,10,endpoint=False,retstep=True)    #ret step
print(a1)


a2=np.logspace(0,10,num=4,endpoint=False)  #log values;base
print(a2)

a2=np.logspace(0,10,num=4,endpoint=False,base=2)  #endpont=fallse;10 not included
print(a2)         #we can give datat type after base