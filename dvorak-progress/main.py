from datetime import datetime
import matplotlib.pyplot as plt

# Date as datetime, speed in words per minute, accuracy float 0 - 1
speeds = [
    (datetime(year=2023, month=11, day=26), 16, None),
    (datetime(year=2023, month=11, day=27), 20, None),
    (datetime(year=2023, month=11, day=28), 23, 0.975),
    (datetime(year=2023, month=11, day=29), 27, 0.9925),
]

def generate_graphs():
    plt.plot([item[0] for item in speeds], [item[1] for item in speeds])
    plt.title("Typing speed progress per day")
    plt.ylabel("Speed (WPM)")
    plt.show()

    plt.plot([item[0] for item in speeds], [item[2] for item in speeds])
    plt.title("Typing accuracy progress per day")
    plt.ylabel("Accuracy")
    plt.show()

