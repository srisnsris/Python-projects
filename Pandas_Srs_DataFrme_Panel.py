import pandas as pd
S=[10,20,30,40,50]
print(pd.Series(S))

#print(pd.Series(S,index=["i","ii","iii","iiii"])) we can change index values

d={'name':['sri','ni','v','as'],'rno':['1','2','3','4']}

print(pd.DataFrame(d))

