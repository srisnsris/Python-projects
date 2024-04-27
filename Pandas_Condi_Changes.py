import pandas as pd
d=pd.read_excel("")   #excel file reading
#excel doc: roll_no, name of student,telugu, eng,math,scienc,social
df=pd.DataFrame(d)
print(df)

df['Total']=df['Tel']+df['Eng']+df['Math']+df['Scie']+df['Soc']
df['Perc']=(df['tot']/500)*100
df["grade"]='None'


"""


]

<40 - Fail
<40 &<60 - Pass
>60 & <70 -first class
>70  - Dis

"""
df.loc[(df['Perc']<40)& (df['Perc']<60)["grade"]]= "PASS"