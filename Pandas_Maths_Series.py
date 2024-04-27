import pandas as pd
a=pd.Series([10,20,30])
b=pd.Series([40,50,60])
print(a)
print( a.add(b))
print( a.sub(b))
print( a.mul(b))
print( a.mod(b))
print( a.le(b))  #boolen
print( a.ge(b))  #vbool
print( a.eq(b))  #bool
print( a.pow(b))
