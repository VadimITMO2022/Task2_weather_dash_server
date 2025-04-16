from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go


def register_callbacks(app):
    @app.callback(
        Output('weather-output', 'children'),
        Output('temp-graph', 'figure'),
        Output('ap-graph', 'figure'),
        Output('o3-graph', 'figure'),
        Output('so2-graph', 'figure'),
        Output('pm2_5-graph', 'figure'),
        Output('pm10-graph', 'figure'),
        Input('city-input', 'value')
    )
    def update_dashboard(city):
        data = load_data(city)
    
        weather_info = html.Div([
            html.H4(f"{data['city_name']}", className="card-title"),
            html.H6(f"{data['date']}", className="card-text"),
            html.Img(src=f"https:{data['icon']}", style={"height": "64px"}),
            html.H5(f"{data['temp']}°C", className="card-subtitle mb-2 text-muted"),
            html.P(data['condition'], className="card-text")
        ])

       
        temp_fig = go.Figure(          
           data=[go.Scatter(x=data['hours'], y=data['co'], mode='lines+markers', name='Температура')],
           layout=go.Layout(title='СO по часам', xaxis_title='Время', yaxis_title='CO (ед.)', template='plotly_dark') 
        )

        temp_fig.update_xaxes ( range = [-0.3,  23.3 ]) 
        temp_fig.update_layout(
        xaxis = dict(
        tickmode = 'linear',
        tick0 = 0.00,
        dtick = 2.00
         )
        )

        ap_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['no2'], mode='lines+markers', name='Атмосферное давление')],
           layout=go.Layout(title='NO2 по часам', xaxis_title='Время', yaxis_title='NO2 (ед.)', template='plotly_dark') 
        )

        ap_fig.update_xaxes ( range = [-0.3,  23.3 ]) 
        ap_fig.update_layout(
        xaxis = dict(
        tickmode = 'linear',
        tick0 = 0.00,
        dtick = 2.00
         )
        )


        o3_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['o3'], mode='lines+markers', name='Атмосферное давление')],
           layout=go.Layout(title='O3 по часам', xaxis_title='Время', yaxis_title='O3 (ед.)', template='plotly_dark') 
        )

        o3_fig.update_xaxes ( range = [-0.3,  23.3 ]) 
        o3_fig.update_layout(
        xaxis = dict(
        tickmode = 'linear',
        tick0 = 0.00,
        dtick = 2.00
         )
        )

        so2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['so2'], mode='lines+markers', name='Атмосферное давление')],
           layout=go.Layout(title='SO2 по часам', xaxis_title='Время', yaxis_title='SO2 (ед.)', template='plotly_dark') 
        )

        so2_fig.update_xaxes ( range = [-0.3,  23.3 ]) 
        so2_fig.update_layout(
        xaxis = dict(
        tickmode = 'linear',
        tick0 = 0.00,
        dtick = 2.00
         )
        )
    
        pm2_5_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm2_5'], mode='lines+markers', name='Атмосферное давление')],
           layout=go.Layout(title='PM2_5 по часам', xaxis_title='Время', yaxis_title='PM2_5 (ед.)', template='plotly_dark') 
        )

        pm2_5_fig.update_xaxes ( range = [-0.3,  23.3 ]) 
        pm2_5_fig.update_layout(
        xaxis = dict(
        tickmode = 'linear',
        tick0 = 0.00,
        dtick = 2.00
         )
        )
    
        pm10_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm10'], mode='lines+markers', name='Атмосферное давление')],
           layout=go.Layout(title='PM10 по часам', xaxis_title='Время', yaxis_title='PM10 (ед.)', template='plotly_dark') 
        )

        pm10_fig.update_xaxes ( range = [-0.3,  23.3 ]) 
        pm10_fig.update_layout(
        xaxis = dict(
        tickmode = 'linear',
        tick0 = 0.00,
        dtick = 2.0
         )
        )
       

        return weather_info, temp_fig, ap_fig, o3_fig,  so2_fig,  pm2_5_fig,  pm10_fig
        