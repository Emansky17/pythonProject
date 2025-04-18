# pythonProject
Data analytics road map Python Project 

# Library

- To install the Pandas library in Python, you can use pip, which is Python's package installer. Here's the command you'd run in your terminal or command prompt:
    pip install pandas

- To install the openpyxl library, which is used for working with Excel files in Python, you can use the pip command. Here's how to do it:
    pip install openpyxl

# GOAL

- Explore pandas library features and funtionality
- Create a program that covert data from CSV, EXCEL JSON etc to dataframe
- Process [Filter, Sort, Slice etc. ] DataFrame

#Remove duplicate:
The drop_duplicates() method in pandas has several parameters that allow you to customize how duplicate rows are identified and removed. Here's an explanation of the key parameters:
- subset:- Specifies which columns to consider when identifying duplicates.
- By default, all columns are used. If you only want to check specific columns, pass a list of column names.
- Example: df.drop_duplicates(subset=['column1', 'column2'])

- keep:- Determines which duplicate to keep or whether to drop all duplicates.
- Options:- 'first': Keeps the first occurrence of each duplicate.
- 'last': Keeps the last occurrence of each duplicate.
- False: Drops all duplicates, leaving only unique rows.

- Example: df.drop_duplicates(keep='last')

- inplace:- If True, modifies the original DataFrame in place, instead of creating a new one.
- Example: df.drop_duplicates(inplace=True)

- ignore_index:- If True, resets the index of the resulting DataFrame. Useful when the original index isn't important.
- Example: df.drop_duplicates(ignore_index=True)





