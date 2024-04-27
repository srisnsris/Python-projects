import pandas as pd
d=pd.read_excel("")   #excel file reading
#excel doc: roll_no, name of student,telugu, eng,math,scienc,social
df=pd.DataFrame(d)
print(df)

#will add new column with total arks of all sub
df['Total_Marks']=df['telugu']+df['eng']+df['math']+df['science']+df['social']  

df.drop(columns="total marks")

df["roll_no","total_Marks"]



#Export DF to excel

pd.to_excel("  give file location ")   #will get index values for Default=True

pd.to_excel("  give file location.xlsx",index=false) #will not get index values for false
pd.to_csv("  give file location.csv",index=false) 
pd.to_excel("  give file location.txt",index=false)

pd.to_excel("  give file location.txt",index=false,sep="\t") 