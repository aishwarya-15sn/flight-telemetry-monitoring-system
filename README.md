# Real-Time Flight Telemetry Monitoring System

A Python-based system for monitoring aircraft telemetry data including altitude, velocity, and geographic position.

The system processes telemetry streams, detects abnormal flight conditions, and visualizes aircraft movement in real time.

## System Architecture

Flight Data Source
        ↓
Telemetry Processor
        ↓
Anomaly Detection Engine
        ↓
Visualization Module

## Features

- Real-time flight telemetry data ingestion
- Telemetry data processing pipeline
- Anomaly detection for abnormal flight conditions
- Visualization of aircraft movement

## Project Structure

data_fetcher.py → Fetch flight telemetry data  
telemetry_processor.py → Process and clean telemetry data  
anomaly_detector.py → Detect abnormal flight conditions  
visualization.py → Display telemetry insights  
main.py → Entry point of the system

## Tech Stack

Python  
Requests  
Pandas  
Matplotlib / Folium

## Example Output

Aircraft: AIC204  
Altitude: 32000 ft  
Velocity: 810 km/h  

No anomalies detected.

## Future Improvements

- Integration with live flight APIs
- Web-based telemetry dashboard
- Advanced anomaly detection models
