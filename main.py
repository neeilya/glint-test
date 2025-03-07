from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import xarray as xr

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dataset = xr.open_dataset("data.nc")

@app.get("/max_wave_height")
def get_max_wave(lat: float, lon: float):
    wave_height = dataset.sel(latitude=lat, longitude=lon, method="nearest")["hmax"].max().item()

    return {
        "latitude": lat,
        "longitude": lon,
        "max_wave_height": wave_height
    }
