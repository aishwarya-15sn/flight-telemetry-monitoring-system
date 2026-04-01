# AeroStream – Real-Time Flight Telemetry Monitoring System

A Python-based system that simulates and processes aircraft telemetry data streams and detects abnormal flight behavior.

## Overview

Aircraft generate continuous telemetry signals such as altitude, velocity and positional coordinates. Monitoring these parameters helps identify abnormal flight conditions early.

AeroStream implements a telemetry processing pipeline that:

• Simulates aircraft telemetry data streams  
• Processes altitude, velocity, temperature and position data  
• Detects anomalies using machine learning (Isolation Forest)  
• Visualizes abnormal flight behavior for monitoring

## System Architecture

Telemetry Generator  
↓  
Telemetry Processing Pipeline  
↓  
Anomaly Detection Engine  
↓  
Visualization Module

## Telemetry Parameters

The system processes the following flight parameters:

- Altitude
- Velocity
- Temperature
- Latitude
- Longitude

## Tech Stack

Python  
Pandas  
NumPy  
Scikit-learn  
Matplotlib  

## Running the System

Install dependencies:
