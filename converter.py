import numpy as np
import pyproj
from pandas import DataFrame
from pyproj import Proj
import pandas as pd
from dms2dec.dms_convert import dms2dec

df = pd.read_csv('coordenadas.csv', sep=',')

myProj = Proj("+proj=utm +zone=30K, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
lat, lon = myProj(df['Latitude'].values, df['Longitude'].values, inverse=True)

UTMx, UTMy = myProj(lat, lon)

df_final = DataFrame(np.c_[lon, lat], columns=['Lat', 'Lon'])

df_final.to_csv("coverted_coordenates.csv")

print(df_final)
