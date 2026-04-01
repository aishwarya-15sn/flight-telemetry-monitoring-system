import matplotlib.pyplot as plt

def plot_results(df):
    print("plotting telemetry data...")
    plt.figure(figsize=(8,6))

    # blue = normal readings, red = detected anomalies
    colors = df["anomaly"].map({1: "blue", -1: "red"})
    plt.scatter(df["altitude"], df["velocity"], c=colors, alpha=0.7)
    plt.xlabel("Altitude (ft)")
    plt.ylabel("Velocity (knots)")
    plt.title("Flight Telemetry Monitoring System")
    plt.grid(True)
    plt.show()