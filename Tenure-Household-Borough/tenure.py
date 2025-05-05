## Importing libraries to analyse data in london
#

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

#%% Cleaning up

all_ta = []


years = [str(x) for x in range(2010,2021)]



for year in years:
    ta = pd.read_excel('tenure-population-borough.xlsx',sheet_name=year,index_col=False,
                      na_values='-' )
    print(f"Reading Year {year},  adding to all_ta")
    rename_cols = {col: ta[col].iloc[0] for col in ta.columns if pd.notna(ta[col].iloc[0])}
    ta = ta.rename(columns=rename_cols)
    ta.columns = ['Code', 'Area'] + list(ta.columns[2:])
    ta = ta.iloc[2:, :7]
    ta = ta.dropna(subset='Code')
    ta = ta[:33]
    ta['Year'] = year

    all_ta.append(ta)
    
    print(f"{year} - has been added to masterfile with ",len(ta), "Records have been added" ) 
    
combined_ta = pd.concat(all_ta, ignore_index=True) 

#%% 

combined_ta = combined_ta.set_index(['Code', 'Area', 'Year'])

combined_ta = combined_ta.drop(columns='Total')

value_varslist = [col for col in combined_ta.columns]

combined_ta = combined_ta.reset_index()

combined_ta = combined_ta.melt(id_vars= ['Code', 'Area', 'Year'],
                               value_vars=value_varslist, 
                               var_name="Housing Category", 
                               value_name="Value"
                               )
combined_ta = combined_ta.set_index(['Code'])

combined_ta['Rank'] = combined_ta.groupby(['Area', 'Year'])['Value'].rank(method='min')

combined_ta.to_csv('Tenure_Analysis.csv')
#%% 





