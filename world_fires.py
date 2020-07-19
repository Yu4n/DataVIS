import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime


filename = './data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)  # header_row = next(reader)

    brgs, lats, lons = [], [], []
    hover_texts = []

    for row in reader:
        lats.append(row[0])
        lons.append(row[1])
        brightness = float(row[2])
        brgs.append(brightness)
        label = f"{datetime.strptime(row[5], '%Y-%m-%d')} - {brightness}"
        hover_texts.append(label)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness / 30 for brightness in brgs],
        'color': brgs,
        'colorscale': 'YlOrRd',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title="World fires")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='World_fires.html')
