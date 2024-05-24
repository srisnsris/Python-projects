import pandas as pd
import openpyxl

#default first sheet
df = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx')
print(df)
print(df.columns)

#loadinf particular sheet
df_sheet_index = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx', sheet_name='Sheet2')
print(df_sheet_index)
#laoding multiple sheets
df_sheet_multi = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx', sheet_name=[0, 'Sheet2'])
print(df_sheet_multi)
#load all sheets
df_sheet_multi = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx', sheet_name=None)
print(df_sheet_multi)
df = pd.DataFrame([[2, 'vinay'], 
                   [3, 'Lilly'], 
                   [4, 'Laxmi']],
index=['one', 'two', 'three'], columns=['Claim', 'Name'])
print(df)

#df.to_excel('Book2.xlsx', sheet_name='Sheet1')


    

