import pandas as pd

s=pd.Series([10,20,30],name="Numbers")
print(s)
s=pd.Series([10,20,30],index=['a','b','c'],name="Numbers")
print(s)

print(s.index)
print(s.array)
print(s.values)
print(s.dtype)
print(s.shape)  
print(s.ndim)
print(s.nbytes)    #only values
print(s.memory_usage)  #will include index and values
print(s.memory_usage(index=False))  #flse ; values
print(s.size)  #3 elemmts
print(s.name)


s1=pd.Series()
print(s1)
print(s1.size)