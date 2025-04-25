import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html
import settings as st


def create_layout():
    return dbc.Container([
       html.Div([
            html.H1("Дашборд погоды в городе", className="header-title"),
            html.H2("Прогноз погоды на сегодня", className="header-description")
        ], className="header"
        ),

        dbc.Row([
            dbc.Col(dbc.Card(id='weather-output', body=True), width=6, xs=12, md=6),
            dbc.Col([
                dbc.Input(id='city-input', 
                          value='Санкт-Петербург', 
                          type='text', placeholder="Введите город", debounce=True),
            ], width=6, xs=12, md=6),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='temp-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='ap-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='co-graph'), width=4, xs=12, md=4),
        ], className="mb-3"),

         dbc.Row([
            dbc.Col(dcc.Graph(id='no2-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='o3-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='so2-graph'), width=4, xs=12, md=4),
        ], className="mb-3"),


    ], fluid=True)


'''
       dbc.NavbarSimple(
            brand="Прогноз погоды 🌦",
            brand_href="#",
            color="primary",
            dark=True,
            className="mb-4 flex justify-content-between",
        ),
'''