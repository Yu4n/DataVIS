import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = './data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# plot high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs)

# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='both', labelsize=16)

plt.show()
