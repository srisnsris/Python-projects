import pandas as pd
#d=pd.read_excel("inlcude path file")   .csv, xlsx
#print(d)  We can load external files; can do manuiplations

d={'Name of Student':['sri','ni','v','as'],
   'Roll no':[1,2,3,4],
   'Telugu':[10,20,30,40],
   'English':[50,60,70,80]}

df=pd.DataFrame(d)
print(df)
