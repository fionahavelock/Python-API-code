from nrfaApi import *
from getMapData import *
import plotly.graph_objects as go
import pandas as pd

df = MapData
df.head()

df['text'] = df['gdf-mean-flow'].astype(str) + '' + df['name']

fig = go.Figure(data=go.Scattergeo(
        locationmode = 'country names',
        lon = df['longitude'],
        lat = df['latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'circle',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Blues',
            cmin = 0,
            color = df['gdf-mean-flow'],
            cmax = df['gdf-mean-flow'].max(),
            colorbar_title="gdf-mean-flow"
        )))

fig.update_layout(
        title = 'gdf-mean-flow',
        geo = dict(
            scope='europe',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )
fig.show()