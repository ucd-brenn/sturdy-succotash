import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

df = pd.read_csv('ClueBase.csv')

def point_maker(c):
    plist = c.split(', ')
    lat = float(plist[0])
    long = float(plist[1])
    return Point(long, lat)

df['geometry'] = df.coord.apply(point_maker)
gdf = gpd.GeoDataFrame(df, geometry = 'geometry', crs = 'EPSG:4326')

gdf.to_crs(epsg = 32613, inplace = True)
ndf = gpd.GeoDataFrame(gdf, geometry = gdf.buffer(10), crs = 'EPSG:32613').copy()
ndf.to_crs(epsg = 4326, inplace = True)

ndf.to_file('points.geojson', driver = 'GeoJSON')
