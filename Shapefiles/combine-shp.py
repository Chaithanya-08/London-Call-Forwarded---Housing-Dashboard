##Import libraries 
import geopandas as gpd 
import os 
import pandas as pd 

#%% 

pm = pd.read_csv('pattymelt.csv')

gdfs = []

folder = 'C:/Users/Chaithanya/Documents/Advanced Policy Analysis/London - Houses/Shapefiles/LB_LSOA2021_shp'

# Loop through all shapefiles
for file in os.listdir(folder):
    if file.endswith(".shp"):
        path = os.path.join(folder, file)
        gdf = gpd.read_file(path)
        gdfs.append(gdf)


#%% 

# Combine all into one GeoDataFrame
london_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True), crs=gdfs[0].crs)

#%%
london_gdf = london_gdf.rename(columns={'lad22cd':'Code', 
                                        'lad22nm':'Area'})
london_gdf = london_gdf.dissolve(by='Code')


#%% Getting a tableau file 

merged_gdf = london_gdf.merge(pm, on='Code')

merged_gdf.to_file("London_Borough_LSOA_All_Variables.geojson", layer="All ",driver="GeoJSON")


#%% Getting a file with max column
#%%



