import requests
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from googlemaps import Client as GoogleMaps
from xgboost import XGBRegressor
import random

# Google Maps API Key (Replace with your own)
# GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
# gmaps = GoogleMaps(GOOGLE_MAPS_API_KEY)

# FastAPI app
app = FastAPI()

# Initialize XGBoost model
model = XGBRegressor()

def get_elevation_data(origin, destination):
    """Fetch elevation gain from Google Maps API"""
    return random.randint(0, 500)  # Placeholder for elevation gain
    # directions = gmaps.directions(origin, destination, mode="driving")
    # polyline = directions[0]["overview_polyline"]["points"]
    # elevation_data = gmaps.elevation_along_path(polyline, 10)
    # elevations = [point["elevation"] for point in elevation_data]
    # elevation_gain = max(elevations) - min(elevations)
    # return elevation_gain

# Define Input Schema
class EVInput(BaseModel):
    battery_capacity: float  # kWh
    efficiency: float  # Wh/km
    weight: float  # kg
    power: float  # kW
    origin: str
    destination: str

@app.post("/predict-range")
def predict_range(input_data: EVInput):
    """Predict EV range based on input parameters and elevation data"""
    elevation_gain = get_elevation_data(input_data.origin, input_data.destination)
    
    # Create feature vector
    features = np.array([[input_data.battery_capacity, input_data.efficiency, 
                          input_data.weight, input_data.power, elevation_gain]])
    
    predicted_range = model.predict(features)[0]
    
    return {"predicted_range_km": predicted_range}

# Sample Training Data (Replace with real-world data)
data = pd.DataFrame({
    "battery_capacity": [50, 60, 75, 90],
    "efficiency": [150, 160, 140, 130],
    "weight": [1500, 1600, 1700, 1800],
    "power": [100, 120, 150, 180],
    "elevation_gain": [100, 200, 300, 400],
    "range_km": [300, 350, 400, 450]
})

# Train XGBoost Model
X = data[["battery_capacity", "efficiency", "weight", "power", "elevation_gain"]]
y = data["range_km"]
model.fit(X, y)

if __name__ == "__main__":
    # import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    range = predict_range(EVInput(
        battery_capacity=75,
        efficiency=140,
        weight=1700,
        power=150,
        origin="New York, NY",
        destination="Los Angeles, CA"
    ))
    print(range)

