# ElevationX - Electric Vehicle Range Prediction

## Overview
ElevationX is a Python-based AI-powered application that predicts the driving range of an electric vehicle (EV) based on:
- Vehicle specifications (battery capacity, efficiency, weight, power)
- Route details (origin, destination, elevation gain)

The application uses Google Maps API to fetch elevation data and a machine learning model to estimate the range.

## Features
- **FastAPI backend** to serve predictions
- **Google Maps API integration** for route and elevation data
- **Linear Regression model** for range estimation
- **REST API** to request predictions

## Installation

### Prerequisites
- Python 3.8 or higher
- Google Maps API Key
- Poetry (for dependency management)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/elevationX.git
   cd elevationX
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```
3. Set up your Google Maps API key in `main.py`:
   ```python
   GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
   ```
4. Run the FastAPI server:
   ```sh
   poetry run uvicorn main:app --reload
   ```

## Usage

### API Endpoint
- **POST** `/predict-range`
- **Request Body (JSON Example)**:
  ```json
  {
    "battery_capacity": 75,
    "efficiency": 140,
    "weight": 1700,
    "power": 150,
    "origin": "San Francisco, CA",
    "destination": "Los Angeles, CA"
  }
  ```
- **Response**:
  ```json
  {
    "predicted_range_km": 400
  }
  ```

## Future Enhancements
- Support for real-time weather impact
- Improved AI model with neural networks
- Web & mobile UI integration

## License
This project is licensed under the MIT License.

