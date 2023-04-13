import streamlit as st
import leafmap.foliumap as leafmap
import xarray as xr
import pydeck as pdk

infile = 'uhr_ascat_velocity.nc'
ds = xr.open_dataset(infile)

st.set_page_config(layout="wide")

st.title("UHR ASCAT Coastal Winds")

map_center=(29,-90)
m = leafmap.Map(center=map_center, zoom=5)
m.add_velocity(ds, zonal_speed='u_wind', meridional_speed='v_wind')

pydeck_layer = m.pydeck_terrain()
st.pydeck_chart(pdk.Deck(layers=[pydeck_layer], initial_view_state=pdk.ViewState(latitude=map_center[0], longitude=map_center[1], zoom=5), height=700))

#m.to_streamlit(height=700)

