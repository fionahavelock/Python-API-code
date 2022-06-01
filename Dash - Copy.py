"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

"""
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State
from timeSeriesPage import *


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "12rem",
    "padding": "1rem 0.5rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "12rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Menu", className="display-4"),
        html.Hr(),
        html.P(
            "North Pennines Water Data", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Using the App", href="/", active="exact"),
                dbc.NavLink("Water Quality", href="/page-1", active="exact"),
                dbc.NavLink("Water Flow", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

#layout of multipage app
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

#Callback for menu page

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return waterFlowPage
    elif pathname == "/page-1":
        return waterFlowPage
    elif pathname == "/page-2":
        return waterFlowPage
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


#callback for water flow page

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
    


if __name__ == "__main__":
    app.run_server(port=8080)