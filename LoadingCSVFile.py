import pandas as pd 

df = pd.read_csv('./annual-enterprise-survey-2023-financial-year-provisional.csv')

#Remove duplicate
df_cleaned = df.drop_duplicates()

# Print the cleaned DataFrame shape
print("Cleaned DataFrame shape:", df_cleaned.shape)


#Filter
filtere_df = df_cleaned[df_cleaned ['Variable_code'] == 'H01']

#print the filtered data
print(filtere_df)



