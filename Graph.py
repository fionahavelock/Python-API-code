from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)
#############################################
#READ RAW WATER 2022 FILE
#change to read from where the data is stored
df = pd.read_csv('C:\\Users\\fgene\\Downloads\\rawwater2022.csv')
###############################################

fig = px.scatter(df, x="Nitrogen, Total Oxidised, Filtered as N", y="CHLOROPHYLL",
                 log_x=True,)

app.layout = html.Div([
    dcc.Graph(
        id='ChlrophyllScatter',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
