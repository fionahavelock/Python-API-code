from dash import Dash, dcc, html, Input, Output, ctx, State, dash_table, callback
import dash_bootstrap_components as dbc
import plotly.express as px
from nrfaApi import *
import pandas as pd
import dash

"""
#Progress
Next stage is link the stattion number to the location, with dictionaries
"""

timeSeriesData = getTimeSeries('cmr', '45001')
df = pd.DataFrame(data=timeSeriesData)
#dropboxValues =  {"Huttons Ambo": 2001, "Leith": 3001, "Kidwelly": 1001}

#app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

waterFlowPage = html.Div([

  
    html.Div([
        dcc.Dropdown(['cmr', 'amax-flow', 'pot-flow', 'gauging-flow'],
        placeholder="Select a flow type",
        id='flowDropdown',)
    
    ]),
    html.Br(),
    html.Div([
        dcc.Dropdown( options = [
       {'label': 'Tyne Spilmersford', 'value': '20003'},
       {'label': 'Kidwelly', 'value': '3001'},
       {'label': 'San Francisco', 'value': '1001'},
        ],
        placeholder="Select a location",
        id='IDdropdown',)
    ]),
    html.Div([
        dbc.Alert(
            "There is no data availble for this query. Please select a different combination.",
            color="warning",
            id="alert-noData",
            dismissable=True,
            is_open=False,
        ),
    ]),
    html.Div([
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            df['Month'].min(),
            df['Month'].max(),
            step=None,
            value=df['Year'].min(),
            marks={str(Month): str(Month) for Month in df['Month'].unique()},
            id='month-slider'
            )
    ]),
    html.Br(),
    html.Div([
        dash_table.DataTable(
        id='metaDataTable',
        columns=[],
        )
    ])
])

"""

@app.callback(
    Output("alert-noData", "is_open"),
    Output('graph-with-slider', 'figure'),
    Output('metaDataTable', 'data'),
    Output('metaDataTable', 'columns'),
    Input('flowDropdown', 'value'),
    Input('IDdropdown', 'value'),
    Input('month-slider', 'value'))
def getUserOptions(flowType, stationNumber, selected_month):
    element_id = ctx.triggered_id if not None else 'No clicks yet'
    global df
    if element_id == 'flowDropdown' or 'IDdropdown' == element_id:
        if flowType != None and stationNumber != None:
            timeSeriesData = getTimeSeries(flowType, stationNumber)
            metaDataFrame = getMetaData(stationNumber)
            metaKey = metaDataFrame.to_dict('records')
            metaValue = [{"name": i, "id": i} for i in metaDataFrame.columns]
            if timeSeriesData == []:
                return True, dash.no_update,  metaKey, metaValue
            df = pd.DataFrame(data=timeSeriesData)
            fig = px.scatter(df, x="Year", y="Value", size="Value")
            return False, fig, metaKey, metaValue
        else:
            return False, dash.no_update, dash.no_update, dash.no_update
    elif element_id == 'month-slider':
        filtered_df = df[df.Month == selected_month]
        fig = px.scatter(filtered_df, x="Year", y="Value", size="Value")
    else:
        return False, dash.no_update, dash.no_update, dash.no_update
    fig.update_layout(transition_duration=500)
    return False, fig, dash.no_update, dash.no_update
    


"""


#if __name__ == '__main__':
    #app.run_server(debug=True)