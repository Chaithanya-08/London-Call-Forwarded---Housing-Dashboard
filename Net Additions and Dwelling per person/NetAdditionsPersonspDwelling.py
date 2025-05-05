#Import Libraries
import pandas as pd 
import matplotlib.pyplot as plt 

housing = [] 

sheets = ['Net additions', 'Persons per dwelling']

#%%

for sheet in sheets: 
    file = pd.read_excel('net-additional-dwellings-total-stock-borough.xlsx',
                                 header=1,sheet_name=sheet, 
                                 dtype=str)
    print(f"Reading  ...{sheet}")
    file = file.loc[1:]
    file.columns = ['Code', 'Area'] + list(file.columns[2:])
    cols = {str(col) :str(col[:4]) for col in file.columns if len(str(col)) > 4 } 
    file = file.rename(columns=cols)    
    file = file.dropna(subset=['Code'])
    file = file.iloc[:33, :22]
    file = file.set_index(['Code','Area'])
    file.to_csv(f"{sheet}.csv")
    print(f"{sheet} - has been extracted to housefile ",len(file), "Records have been created")
    print(file.head())




#%%
