d=pd.read_excel("")   #excel file reading
#excel doc: roll_no, name of student,telugu, eng,math,scienc,social
df=pd.DataFrame(d)
print(df)

#accessing rows
#first five rows
df.head()  #first five ris defalt
df.head(7)  #will get 7 rows; 
df.tail()   #$last 5 rows;parmates can give

df.describe()  #will give count, mean,std, min vale,25%, 75%, max
df.colums  #will give column names
df.shape()  #rows columns
df['column name']  #only partic col will display; can give no of columns

df['col name'].head()  #display first 5

df[1:10]  #will display 10 rows

df[1:10:2] #2 is step sixe; will skip 2 rows
df(['colname','name','telug']) [1:6]  #slicing  [5:] 5to end

df.loc[1]  #will change format


for index,rows  in df.iterrows():
    print(index,rows)    

for index,rows  in df.iterrows():
    print(index,rows['columnanme'])
    
df.loc(df['col name']==105)   #105 data of parti col; slicing

    












