import matplotlib.pyplot as plt
import numpy as np


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

# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")

plot_streamflow(dates, flows, sites)
