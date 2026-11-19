import matplotlib.pyplot as plt
import numpy as np
import csv

def load_streamflow(filename):
    data = np.genfromtxt(filename,
                     delimiter=",", dtype=str, skip_header=1)

    x = data[:, 0]
    y_1 = data[:, 1].astype(float)
    y_2 = data[:, 2].astype(float)
    y_3 = data[:, 3].astype(float)
    y_4 = data[:, 4].astype(float)
    y_5 = data[:, 5].astype(float)

    flows = np.column_stack((y_1, y_2, y_3, y_4, y_5))
    return x, flows

# ChatGPT helped load the streamflow data and separate the columns.
# Each column represents a date or a different river monitoring site.


# ChatGPT helped fix the x-axis labels and graph formatting.
# Each line represents streamflow at a monitoring site.

def plot_streamflow(dates, flows, sites):
    plt.figure(figsize=(12, 6))


    positions = range(len(dates))


    plt.plot(positions, flows[:, 0], label=sites[0])
    plt.plot(positions, flows[:, 1], label=sites[1])
    plt.plot(positions, flows[:, 2], label=sites[2])
    plt.plot(positions, flows[:, 3], label=sites[3])
    plt.plot(positions, flows[:, 4], label=sites[4])

    plt.title("Provo River Streamflow Data (2021)")
    plt.xlabel("Date")
    plt.ylabel("Streamflow (cfs)")

# Show fewer dates so the labels do not overlap.
    ticks = np.linspace(0, len(dates)-1, 8, dtype=int)
    plt.xticks(ticks, dates[ticks], rotation=45)

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()
def summarize(dates, flows, sites):


    """Calculate and display streamflow statistics for each monitoring site."""
    # Spreadsheet check for gauge 10163000:
    # MAX = 131.0 cfs
    # AVERAGE = 56.95236111111111 cfs
    # These values match the Python calculations.
        # Create a fresh CSV file with column headings
    with open("streamflow_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Gauge", "Max (cfs)", "Date of max", "Min (cfs)", "Avg (cfs)"])
    print("Streamflow Summary Statistics:")
    print(f"{'Gauge':<12} {'Max (cfs)':>10} {'Date of max':<20} {'Min (cfs)':>10} {'Avg (cfs)':>10}")
    for i, site in enumerate(sites):
        site_flows = flows[:, i]
        max_flow = np.max(site_flows)
        min_flow = np.min(site_flows)
        avg_flow = np.mean(site_flows)
        max_index = np.argmax(site_flows)
        max_date = dates[max_index]
        print(f"{site:<12} {max_flow:>10.1f} {max_date:<20} {min_flow:>10.1f} {avg_flow:>10.1f}")

        # Save the statistics for this gauge to the CSV file
        with open("streamflow_summary.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([site, max_flow, max_date, min_flow, avg_flow])
# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")

plot_streamflow(dates, flows, sites)

summarize(dates, flows, sites)

# Ask the user for a streamflow threshold in cfs
threshold = float(input("Enter a flow threshold (cfs): "))

# Calculate how many hours each gauge exceeded the threshold
for i, site in enumerate(sites):
    hours = np.sum(flows[:, i] > threshold) * 0.25
    print(f"Gauge {site}: {hours:.2f} hours above {threshold} cfs")