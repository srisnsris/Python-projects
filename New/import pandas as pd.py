import pandas as pd
import openpyxl

#default first sheet
df = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx')
print(df)
'''#print(df.columns)

#loadinf particular sheet
df_sheet_index = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx', sheet_name='Sheet2')
print(df_sheet_index)
#laoding multiple sheets
df_sheet_multi = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx', sheet_name=[0, 'Sheet2'])
print(df_sheet_multi)
#load all sheets
df_sheet_multi = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx', sheet_name=None)
print(df_sheet_multi)
'''
#  {'Claim': '3', 'Name': 'Alice'},{'Claim': '3', 'Name': 'Alice'}
    # Add more rows here as needed
df1 = pd.concat([df, pd.DataFrame([{'Claim':'2','Name':'Vinay'}])],ignore_index=True)
print(df1)
df1.to_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx', index=False)
print("Modified DataFrame saved to 'Book2.xlsx'")

#how to remove duplicates 
import pandas as pd
# Read the Excel file into a DataFrame
df = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx')
# Remove duplicate rows based on all columns
df.drop_duplicates(inplace=True)
# Save the modified DataFrame back to the Excel file
df.to_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx', index=False)
print("Modified DataFrame saved to 'Book2.xlsx'")
 
 # how to remove particular rows
 import pandas as pd
# Read the Excel file into a DataFrame
df = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx')
# Drop the row with index 2
df1 = df.drop(index=2)
# Save the modified DataFrame back to the Excel file
df1.to_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx', index=False)
print("Modified DataFrame saved to 'Book2.xlsx'")

# how to filter data and save to other Excel file
import pandas as pd

# Read the original Excel file into a DataFrame
original_df = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx')

# Filter rows where 'Claim' values are greater than 1
filtered_df = original_df[original_df['Claim'] > 1]
print(filtered_df)
# Save the filtered DataFrame to a new Excel file
filtered_df.to_excel(r'C:\Users\srinu\OneDrive\Desktop\Filtered_Book2.xlsx', index=False)
print("Filtered data saved to 'Filtered_Book2.xlsx'")

