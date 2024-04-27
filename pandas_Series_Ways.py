import numpy as np
import pandas as pd

sd=pd.Series()
#print(sd)#
sd

l=[10,20,30,40]
sd=pd.Series(l)
print(sd)

sd=pd.Series(l,index=['a','b','c','d'])  #we can give index to values
print(sd)


a=np.array([50,60,70,80])
print(a)

sa=pd.Series(a)

print(sa)

d={'a':10,'b':20,'c':30,'d':40}    #dic
pd.Series(d)

dt=[('a',10),('b',20),('c',30),('d',40)]  #dic can represent list of tuples
pd.Series(dt)