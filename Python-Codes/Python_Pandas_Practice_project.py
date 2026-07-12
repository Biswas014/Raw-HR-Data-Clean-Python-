import pandas as pd
import numpy as np
from word2number import w2n

#1. Dataset Exploration
df = pd.read_csv("messy_HR_data(pandas).csv")
# print("\nRaw file")
# print(df)

# print(df.head(10))   #top 10 rows
# print(df.shape)     #size of the dataset
# print(df.tail(15))       # last 15 rows
# print(df.info())
# print(df.describe())     #statistics acoross all columns
# print(df.columns)       # column headers
# print(df.columns.dtype) # datatype of the column labels (column names)
    # It is NOT talking about the data inside the dataframe.
# print(df.dtypes) # Datatype of each column's data

# print(df.iloc[6]) #indexing to go exact 7th row
# print(df.loc[6]) #exact 6th index row
# print(df.nunique()) #no of unique values per clm
# print(df['Age'].nunique())    #no of unique values in age clm

# print(df.isnull().sum()) #no of missing(nan) values clm wise(age, email, phone no)
# print(df.isnull().mean()*100)    # % of missing values for every clm
# print(df.isnull().any())   #check which columns have any null valeus(NaN) return in boolean
    
    # check how many nulls & whitespaces available for every string column
# for col in df.select_dtypes(include='object'):
#     print(col, ((df[col].notna()) & (df[col].str.strip() == '')).sum())



#2. Data Preparation
 
 # (a).handling duplicates
# print(df.duplicated().sum()) #count duplicate rows
# print(df[df.duplicated(keep= False)]) #see every duplicate row(include the first)
   # by default, (keep = true) means don't show the first row
# #remove duplicate rows
# df.drop_duplicates(inplace= True)

 #(b) remove leading & trailing spaces
## Select only columns with object (string) data types
# str_cols = df.select_dtypes(include='object').columns
# # Apply .str.strip() to just those columns
# df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())
# to ensure spaces has been removed
# # df['Name_Length'] = df['Name'].str.len().fillna(0).astype(int)  

# #(c) case changes and create the full name removing middle spaces
# df['Name'] = df['Name'].str.title()
# df['Email'] = df['Email'].str.lower()
# df['Department'] = df['Department'].str.upper()
# df['Position'] = df['Position'].str.title()
# df['Name'] = df['Name'].str.split().str.join(' ')

# # (d) handles special characters & empty values
# # ^\s*$ means: "from start (^) to end ($), contain only whitespace (\s) zero or more times (*)"
# df['Phone Number'] = df['Phone Number'].replace(r'^\s*$', np.nan, regex=True)
# # to replace special characters from phone no column
# df['Phone Number'] = df['Phone Number'].str.replace(r'[^0-9]', '', regex=True)
# #replace missing values of email and phone no to 'Unknown'
# df['Phone Number']= df['Phone Number'].replace(np.nan,'Unknown',inplace= True)
# df['Email'] = df['Email'].replace(np.nan,'Unknown',inplace= True)

# # (e) Replace inconsistent department names.

# #  # show all unique departments
# #  print(df['Department'].unique())

# mapping = {
#     'INFORMATION TECHNOLOGY':'IT',
#     'HUMAN RESOURCES':'HR',
#     'FINANCE':'Finance',
#     'MARKETING':'Marketing',
#     'SALES':'Sales'
# }
# df['Department'] = df['Department'].replace(mapping)

# # (f) change age and salary values in words to numbers

# # define a helper function 
# def clean_word_to_num(val):
#     # Catch existing Nulls
#     if pd.isna(val): 
#         return np.nan

#     # Standardize the Text   
#     val_str = str(val).strip().lower()
#     if val_str in ["", "nan", "none"]: 
#         return np.nan

#     # Check for Pure Digits   
#     try:
#         if val_str.isdigit():
#             return int(val_str)
        
#         # if not, translate Words to Numbers
#         return w2n.word_to_num(val_str)
    
#     # changes any different type of text like 'unknown' to 'nan'
#     except ValueError:
#         return np.nan

# # Apply the transformation function to both columns
# df['Age'] = df['Age'].map(clean_word_to_num)
# df['Salary'] = df['Salary'].map(clean_word_to_num)

# # (g) converting the data types and replaces missing values with mean or median
# # Safely parse columns into numeric values (converts any remaining anomalies to NaN)
# df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
# df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# # Calculate metrics (Pandas automatically ignores the NaNs here)
# avg_age = df['Age'].mean()
# median_salary = df['Salary'].median()

# # Impute missing values with the calculated mean and median
# df['Age'] = df['Age'].fillna(avg_age)
# df['Salary'] = df['Salary'].fillna(median_salary)

# # change the age data type into int
# df['Age'] = df['Age'].round(0)
# df['Age'] = df['Age'].astype('Int64')

# convert date column into datetime column
# df['Joining Date'] = pd.to_datetime(df['Joining Date'], format='mixed', errors='coerce')

# Important questions can be asked in an interview
#(a) which employees have been working in finance department having salary below the average
# finance_below_average = df[(df['Salary'] < df['Salary'].mean()) & (df['Department'] == 'Finance')]
# print(finance_below_average)

# (b) employees who have working in hr or marketing
# hr_or_marketing=df[df["Department"].isin(["HR","Marketing"])]
# print(hr_or_marketing)

# (c) no of employees joined each year
# print(df['Year'].value_counts())

# (d)count how many employees has been working in sales dept
# df[df['Department'] == 'Sales'].value_counts()

#(e) which performance score is most common
# print(df['Performance Score'].value_counts().sort_values(ascending= False).head(1))

# (f) which joining month has the highest recruitment
# df['Month'] = df['Joining Date'].dt.month
# print(df['Month'].value_counts().sort_values(ascending= False).head(1))

#(g) which gender has highest average salary
# print(df.groupby('Gender')['Salary'].mean().round(2).sort_values(ascending= False).head(1))



# create a csv file and Export the cleaning file 
# df.to_csv("Cleaned_HR_data.csv",index= False)
# load_df = pd.read_csv("Cleaned_HR_data.csv")
# print(load_df)