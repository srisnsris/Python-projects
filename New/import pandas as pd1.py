import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel(r'C:\Users\srinu\OneDrive\Desktop\Book2.xlsx')

# Filter rows where 'Claim' values are greater than 1
filtered_df = df[df['Claim'] > 1]

# Print the filtered DataFrame to verify correctness
print(filtered_df.head())

# Save the modified DataFrame back to the Excel file
filtered_df.to_excel(r'C:\Users\srinu\OneDrive\Desktop\Filtered_Book2.xlsx', index=False)

print("Filtered DataFrame saved to 'Filtered_Book2.xlsx'")