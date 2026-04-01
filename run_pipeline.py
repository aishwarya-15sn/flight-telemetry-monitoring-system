from telemetry_generator import generate_telemetry
from anomaly_detector import detect_anomalies
from visualize import plot_results

def main():
    data = generate_telemetry()
    results = detect_anomalies(data)
    plot_results(results)

if __name__ == "__main__":
    main()