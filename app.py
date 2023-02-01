import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from modules.utils import Header, make_dash_table
import pandas as pd
from pathlib import Path
import modules.portfolio_data as pfd


df_tech = pd.read_csv(Path("Resources/Test.csv"))
df_a_data = pd.DataFrame(pd.read_csv(Path("Resources/INFY_data.csv")))

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.title = "Portfolio Analyzer"
app._favicon = ("assets/favicon.ico")
server = app.server

global_value = []

# Describe the layout/ UI of the app
app.layout = html.Div([
    
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Portfolio Analyzer"),
                                    html.Br([]),
                                    html.P(
                                        "Welcome to Columbia University's first ever all-student created portfolio analyzer.\
                                        Please take advantage of our great, powerful, multi-use web application to it's full extent. \
                                        Only one thing we must ask of you is share and give proper credit to our organization when using at a corporate level. \
                                        More-over take a peek at all our features and hope you achieve greatness with the tools at hand.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    html.Div(
                        [
                            dcc.Store('memory-intervals', storage_type='session'),
                            dcc.Dropdown(['INFY', 'OCLA', "AAPL", 'GOOG'], id='demo-dropdown', placeholder= "Please Choose One", multi=True, persistence= True, persistence_type="session")
                            ]),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Portfolio Overview"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_tech)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Portfolio Versus S&P 500",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=df_a_data["Date"],
                                                    y=df_a_data["Close"],
                                                    marker={
                                                        "color": "#0849A3",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Portfolio Value",
                                                ),
                                                go.Bar(
                                                    x=df_a_data["Date"],
                                                    y=df_a_data["Close"],
                                                    marker={
                                                        "color": "#dddddd",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="S&P 500 Index",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0228945952895,
                                                    "y": -0.189563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 10,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=330,
                                                xaxis={
                                                    "autorange": True,
                                                    "range": ["2000-01-01", "2023-01-01"],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "date",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 100],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": True},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Overall Portfolio Performance",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=pfd.get_historical_data("INFY").index,
                                                    y=pfd.get_historical_data("INFY")["Close"],
                                                    line={"color": " #0849A3"},
                                                    mode="lines",
                                                    name="INFY",
                                                ),
                                                go.Scatter(
                                                    x=pfd.get_historical_data("ORCL").index,
                                                    y=pfd.get_historical_data("ORCL")["close"],
                                                    line={"color": " #0849D9"},
                                                    mode="lines",
                                                    name="ORCL",
                                                )
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                title="",
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=340,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0277108433735,
                                                    "y": -0.142606516291,
                                                    "orientation": "h",
                                                },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 50,
                                                },
                                                showlegend=True,
                                                xaxis={
                                                    "autorange": True,
                                                    "range": ["2000-01-01", "2023-01-01"],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "date",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 100],
                                                    "showline": True,
                                                    "title": "$",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": True},
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Portfolio Prediction",
                                        className="subtitle padded",
                                    ),
                                    html.Img(src= app.get_asset_url("favicon.ico"), height = 100, width = 150),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Risk Analysis"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_tech)),
                                ],
                                className="six columns",
                            ),
                            html.Div(id="output_container", children=[])
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )

# Update page
@app.callback(
    Output('memory-intervals', 'data'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return global_value.append(value)
    
def display_page(app):
   return app

if __name__ == "__main__":
    app.run_server(debug=True)