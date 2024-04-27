import pandas as pd
d=pd.read_excel("")   #excel file reading
#excel doc: roll_no, name of student,telugu, eng,math,scienc,social
df=pd.DataFrame(d)
print(df)


#will display boolean-T or F

df.duplicated()

#removing dups#will ceate ne data frame after remov data frames

df.drop_duplicates()

/#will update in original data set

df.drop_duplicates(inplace=True)



