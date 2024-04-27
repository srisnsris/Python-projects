import pandas as pd
d=pd.read_excel("")   #excel file reading
#excel doc: roll_no, name of student,telugu, eng,math,scienc,social
df=pd.DataFrame(d)
print(df)

df.loc[3]
df.loc[3,'name_of_student']  #retrive data based on selct method;argumens


df.iloc[0:4,1:7]   #index based retriv;disply 4 rows, 7 colmns





