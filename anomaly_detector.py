import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    print("running anomaly detection...")
    features = df[["altitude", "velocity", "temperature", "latitude", "longitude"]]
    model = IsolationForest(contamination=0.02, random_state=42)
    model.fit(features)
    preds = model.predict(features)
    df["anomaly"] = preds
    weird_points = df[df["anomaly"] == -1]
    print("number of anomalies detected:", len(weird_points))
    return df