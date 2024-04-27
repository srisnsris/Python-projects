import pandas as pd
d=pd.read_excel("")   #excel file reading
#excel doc: roll_no, name of student,telugu, eng,math,scienc,social
df=pd.DataFrame(d)
print(df)

df.sort_values("name of student")

df.sort_values("Maths")

df.sort_values("name of student",ascending=False)

df.sort_values("name of student","Maths",ascending=[1,0])











