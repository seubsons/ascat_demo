import streamlit as st
#import leafmap.foliumap as leafmap
import leafmap.leafmap as leafmap
import xarray as xr
import numpy as np
import netCDF4

#infile = 'uhr_ascat_velocity.nc'
ds = xr.open_dataset('uhr_ascat_velocity.nc')
#st.write(ds)
##################################################################
#st.set_page_config(layout="wide")
st.set_page_config()

# Customize page title
st.title("UHR ASCAT Coastal Winds")

map_center=(29,-90)
m = leafmap.Map(center=map_center, zoom=5)

# m.add_basemap("HYBRID", show=False)
# m.add_basemap("Esri.WorldStreetMap", show=False)
# m.add_basemap('CartoDB.DarkMatter', show=False)

m.add_velocity(ds, zonal_speed='u_wind', meridional_speed='v_wind')

#m.to_streamlit(height=700)
m.to_streamlit()
