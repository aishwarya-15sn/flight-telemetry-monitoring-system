# Flight Telemetry Monitoring System

A Python-based telemetry monitoring pipeline that simulates aircraft flight data and detects abnormal flight behavior using anomaly detection algorithms.

## Overview

Modern aircraft generate continuous telemetry streams from onboard sensors. Monitoring these signals helps identify abnormal flight conditions early.

This project simulates a telemetry processing pipeline that:

• Generates synthetic aircraft telemetry data  
• Processes altitude, velocity, temperature and positional readings  
• Detects abnormal patterns using an Isolation Forest model  
• Visualizes anomalies in flight telemetry  

## Telemetry Parameters

The system processes the following flight parameters:

- Altitude (ft)
- Velocity (knots)
- Temperature
- Latitude
- Longitude

## Architecture

Telemetry Generator  
↓  
Data Processing Pipeline  
↓  
Anomaly Detection (Isolation Forest)  
↓  
Visualization of abnormal flight behavior

### System Modules

1. Telemetry Generator – Simulates aircraft telemetry streams  
2. Telemetry Processor – Prepares telemetry data for analysis  
3. Anomaly Detector – Identifies abnormal flight behaviour using Isolation Forest  
4. Visualization Module – Highlights anomalies in flight telemetry plots
## Technologies Used

Python  
Pandas  
NumPy  
Scikit-learn  
Matplotlib

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the telemetry monitoring pipeline:

python src/run_pipeline.py

## Output

The system detects abnormal telemetry readings and visualizes them:

Blue → Normal telemetry  
Red → Detected anomalies

## Future Improvements

- Real-time telemetry stream ingestion
- Integration with aircraft sensor datasets
- Alerting system for critical anomalies

## Example Output

Example anomaly detection visualization from the telemetry monitoring system.

![Telemetry Output](assets/telemetry_output.png)
