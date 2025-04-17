import pandas as pd
import os

file_path = './annual-enterprise-survey-2023-financial-year-provisional.xlsx'

if os.path.exists(file_path):
    df = pd.read_excel(file_path, sheet_name='annual-enterprise-survey-2023-f')
else:
    print(f"File not found: {file_path}")

# Display the first few rows of the DataFrame
print(df.head())

#Convert Value to numeric
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')


#SORT descending order
df_sorted = df.sort_values(by = 'Value', ascending=False)

#Display the first few row of the sorted DataFrame
print(df_sorted.head())

#Filter with less than and greater than operator
df_filtered = df[(df['Value'] > 500 ) & (df['Value'] < 1000)]

#Filter and sort
df_sorted_filtered = df_filtered.sort_values(by = 'Value', ascending=True)
    
#Display
print(df_sorted_filtered.head())

#Sample 5 rows
Sampled_rows = df_sorted_filtered.sample(n=5, random_state = 1)

#Check sample date
print(Sampled_rows)

# Save the sampled rows to a text file
Sampled_rows.to_csv('sampled_rows.txt', sep='\t', index=False)  # Use tab as the delimiter