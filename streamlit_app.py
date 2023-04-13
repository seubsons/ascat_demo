import streamlit as st
import leafmap.foliumap as leafmap
import xarray as xr
import numpy as np
import ncdf_velocity

infile = 'test_file.nc'
dsx = xr.open_dataset(infile)

ds3 = ncdf_velocity.convert(dsx)

##################################################################
st.set_page_config(layout="wide")

# Customize page title
st.title("UHR ASCAT Coastal Winds")

map_center=(29,-90)
m = leafmap.Map(center=map_center, zoom=6)

m1.add_velocity(ds3, zonal_speed='u_wind', meridional_speed='v_wind')

m.add_basemap("HYBRID", show=False)
m.add_basemap("Esri.WorldStreetMap", show=False)
m.add_basemap('CartoDB.DarkMatter', show=True)


m.to_streamlit(height=700)