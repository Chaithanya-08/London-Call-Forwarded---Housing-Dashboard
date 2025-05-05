##Income Analysis 
# 

import pandas as pd 
import matplotlib.pyplot as plt 

#% Reading all the files 
income = pd.read_excel('earnings-workplace-borough.xlsx', sheet_name='All workers',
                       dtype=str)


#Cleaning up the files for ALL FT Weekly Workers 
col_names = {income.columns[0] : "Code", income.columns[1] : "Area"}

#Deleting the first row 
income = income.iloc[1:].reset_index(drop=True) 

#Changing the name of all the columns with the list 
income = income.rename(columns=col_names) 

#Converting all the columns
income.columns = income.columns.astype(str)

#Getting a list of unnamed columns within the income dataframe 
no_cols = [col for col in income.columns if 'Unnamed' in col]

#Deleting alll the unknown columns to keep 
income = income.drop(columns=no_cols)

#Filter for the first 33 rows 
income = income[:33]

#Setting Code and Area as the indices 
income = income.set_index(['Code', 'Area'])

#Calculating the annual median for income 
year_list = [col for col in income.columns]

#Making data numeric
for col in year_list:
    income[col] = pd.to_numeric(income[col], errors='coerce')

#Converting to year 
income = income* 52

#CSV
income.to_csv('Income.csv')


#%% 
