import pandas as pd


melt_files = ['Income.csv', 'Net additions.csv', 'Persons per dwelling.csv', 
              'Rent.csv', 'Waiting_list.csv']

meltdfs = [x.replace(".csv", " ").strip("  ") for x in melt_files]

melt_dictionary = {k:v for k,v in zip(melt_files,meltdfs)}


#%%
def melt(file, meltdfs) -> str:
    df = pd.read_csv(file)
    df_melt = df.melt(id_vars=['Code', 'Area'], var_name='Year', value_name=meltdfs)
    df_melt = df_melt.set_index(['Code', 'Area', 'Year'])
    return df_melt

#%%

files = []

for k,v in melt_dictionary.items(): 
   files.append(melt(k,v))
   
#%% 

patty_melt = pd.concat(files, axis=1, ignore_index=False)
 
patty_melt['Income/Rent ratio'] = patty_melt['Income'] / patty_melt['Rent']

patty_melt.to_csv('pattymelt.csv')

#%%
