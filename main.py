from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import xarray as xr
import numpy as np

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
    try:
        wave_height = dataset.sel(latitude=lat, longitude=lon, method="nearest")["hmax"].max().item()

        if np.isnan(wave_height):
            raise ValueError("No wave data available at this location (likely land).")

        return {
            "latitude": lat,
            "longitude": lon,
            "max_wave_height": wave_height
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))