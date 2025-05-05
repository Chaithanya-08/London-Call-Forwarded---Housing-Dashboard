## Understanding the pattern of waiting lists 
#

# One graph to show trends of waiting lists within London, 
# 

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import geopandas as gdp

#% Cleaning up waiting list - Households

wait = pd.read_excel('households-on-local-authority-waiting-list.xlsx',
                          sheet_name='Households on LA Waiting List', 
                          dtype=str)

#%% Non standard clean up the waiting list 

#Creating a dictionary of columns that need to have a name
no_cols = {col: wait[col].iloc[0] for col in wait.columns if 'Unnamed' in col}


#%% Cleaning up the waiting list file

#Renaming the wait_list columns
wait = wait.rename(columns=no_cols)

#Dropping Empty columns
wait = wait.drop(index=[0,1])

#Dropping Code Column 
wait = wait.drop('Code',axis=1)

#Renaming 'actual code column' 
wait.rename(columns={wait.columns[0]: 'Code', 
                     wait.columns[2]: '1997'}, inplace=True)

#Dropping null values 
wait = wait.dropna(subset='Code')

#Now First 33 are all London Boros 
wait = wait[:33]

#CSV 
wait.to_csv('Waiting_list.csv', index=False)

#%%

