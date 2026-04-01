import pandas as pd
import numpy as np

def generate_telemetry():
    print("generating simulated flight telemetry...")
    rows = 500
    altitude = np.random.normal(35000, 1200, rows)
    velocity = np.random.normal(500, 40, rows)
    temperature = np.random.normal(-40, 4, rows)
    latitude = np.random.normal(40, 0.5, rows)
    longitude = np.random.normal(-74, 0.5, rows)
    df = pd.DataFrame({
    "altitude": altitude,
    "velocity": velocity,
    "temperature": temperature,
    "latitude": latitude,
    "longitude": longitude
    })

    # introduce a few abnormal readings
    df.loc[50, "altitude"] = 45000
    df.loc[120, "velocity"] = 700
    df.to_csv("data/telemetry_data.csv", index=False)
    print("telemetry data saved to data/telemetry_data.csv")
    return df