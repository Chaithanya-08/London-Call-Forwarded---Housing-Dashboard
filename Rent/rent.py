#Import libraries 

import pandas as pd 


#%% Non Standard clean up of rent

#Skipping the first row, reading the Xlsx file
rent = pd.read_excel('social-landlord-rents-borough.xlsx',sheet_name='RSL Rents')

#Dropping the first row - to keep
rent = rent.tail(-1)

#Dropping col code,
rent = rent.drop(columns='Code')

#Renaming the new code
rent = rent.rename(columns={'New Code':'Code'})

#Keep the first 33 
rent = rent[:33]

#Setting index 
rent = rent.set_index(['Code', 'Area'])

#Multiply by 4 to get monthly rent 
rent = rent*52

#CSV 
rent.to_csv('Rent.csv', index=True)

#%%