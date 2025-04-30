import pandas as pd


#data = {
#    'Industry_name_NZSIOC': ['Alice', 'Bob', 'Charlie', 'David'],
#    'Value': [24, 27, 22, 32],
#    'Variable_category': ['New York', 'Los Angeles', 'Chicago', 'Houston']
#}

#df = pd.DataFrame(data)

file_path = 'annual-enterprise-survey-2023-financial-year-provisional.xlsx'
df = pd.read_excel(file_path)

#print all data in tabular
print(df)

print('=====================')

#Accessing a sinle column 
print(df['Industry_name_NZSIOC'])

print('=====================')

#Accssing multiple column
print(df[['Industry_name_NZSIOC', 'Variable_category']])

print('=====================')

#Accesing Row by index label
print(df.loc[0])

print('=====================')

#Accessing multitple rows by index
print(df.loc[0:2])

print('=====================')

# Get rows where Value is greater than 25
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
print(df[df['Value'] > 25])

print('=====================')

#Set 'Industry_name_NZSIOC as the index
df.set_index('Industry_name_NZSIOC', inplace=True)
print(df)

print('=====================')

#indexing with `at`
#Accessing as single value
print(df)
print(df.empty)
print(df.index)
print(df.iloc[0]['Variable_category'])
df.reset_index(drop=True, inplace=True)

print('=====================')
print(df.at[0, 'Variable_category'])   # Variable_category of the first row


print('=====================')
#Accessing a single value
print(df.shape)
print(df)
print(df.columns)
print(df.iat[0, 0])  # Access the first row, first column
print(df.iat[0, 1])  # Access the first row, second column
#print(df.iat[0, 2]) #Variable_category of the first row (2nd column)

print('=====================')

# Slicing rows
print(df[1:3])  # Rows 1 and 2

# Slicing columns
print(df.loc[:, 'Value':'Variable_category'])  # All rows, columns from 'Value' to 'Variable_category'


print('=====================')
#Multi Index
arrays = [
    ['A', 'A', 'B', 'B'],
    ['one', 'two', 'one', 'two']
]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
df_multi = pd.DataFrame({'value': [1, 2, 3, 4]}, index=index)
print(df_multi)

# Accessing data in MultiIndex
print(df_multi.loc['A'])