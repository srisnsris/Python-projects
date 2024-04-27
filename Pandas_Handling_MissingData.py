import pandas as pd
d=pd.read_excel("")   #excel file reading
#excel doc: roll_no, name of student,telugu, eng,math,scienc,social
df=pd.DataFrame(d)
print(df)


#rows with missing data will remove; original data not affect
pd.dropna(df)


#reflect orginal data not like dropna
pd.dropna(inplace=True)


#display will not get missing data
df['Telugu'].dropna()
#missing data will deleted
df.loc[:,['telugu','english']].dropna()

df.fillna("Missing")

#will fill the data for missing data;giving inputs

df['Telugu'].fillna(40)

df.loc[:,['Telugu','English']].fillna(45)


#mean data will apply to missing data; std dev 
df['Telugu'].fillna(df['Telugu'].mean())