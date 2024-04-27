import pandas as pd
d=pd.read_excel("")   #excel file reading
#excel doc: roll_no, name of student,telugu, eng,math,scienc,social
df=pd.DataFrame(d)
print(df)

df.loc[df['Telugu']<60]   
df.loc[df['eng']<60]
df.loc[df["Telugu"]<60 & df["English"]<60] #need to use & symbol not AND
df.loc[(df["Telugu"]>80)&df["Eng"]>80 & df["Maths"]>80]
df.loc[df["Name of stud"].str.contains("t")]
df.loc[~df["Name of stud"].str.contains("t")]  #~ doesn't contains S
df.loc[df["Name of stud"].str.startswith("t")] 
df.loc[~df["Name of stud"].str.startswith("t")] 

df.loc[~df["Name of stud"].str.endswith("t")] 
df.loc[df["Name of stud"].str.endswith("t")] 


