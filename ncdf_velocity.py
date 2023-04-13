import numpy as np
import xarray as xr

def convert(dsx):
    ds3 = xr.Dataset(
    {
        "speed": (("lat", "lon"), dsx['speed'].data),
        "dir": (("lat", "lon"), dsx['dir'].data),
    },
    coords={"lat": np.arange(1142), "lon": np.arange(1235)},
    )
    wspeed = ds3['speed'].data
    wdir = ds3['dir'].data
    u_wind = wspeed*np.sin(wdir*np.pi/180)
    v_wind = wspeed*np.cos(wdir*np.pi/180)
    ds3["u_wind"] = (("lat", "lon"), u_wind)
    ds3["v_wind"] = (("lat", "lon"), v_wind)
    
    lat = dsx['lat'].mean(dim=["wvcs"]).data
    lon = dsx['lon'].mean(dim=["rows"]).data
    
    ds3 = ds3.assign_coords(lat=lat, lon=lon)
    
    return ds3