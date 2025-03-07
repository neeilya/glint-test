from fastapi import FastAPI
import xarray as xr

app = FastAPI()

dataset = xr.open_dataset("data.nc")

@app.get("/max_wave_height")
def get_max_wave(lat: float, lon: float):
    wave_height = dataset.sel(latitude=lat, longitude=lon, method="nearest")["hmax"].max().item()

    return {
        "latitude": lat,
        "longitude": lon,
        "max_wave_height": wave_height
    }
