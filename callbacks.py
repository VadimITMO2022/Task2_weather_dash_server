from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
import settings as st
import plotly.io as pio


def register_callbacks(app):
    @app.callback(
        Output('weather-output', 'children'),
        Output('temp-graph', 'figure'),
        Output('ap-graph', 'figure'),
        Output('co-graph', 'figure'),
        Output('no2-graph', 'figure'),
        Output('o3-graph', 'figure'),
        Output('so2-graph', 'figure'),
        Input('city-input', 'value')
    )
    def update_dashboard(city):
        data = load_data(city)
    

        weather_info = html.Div([
            html.H4(f"Город:  {data['city_name']}", className="card-title"),
            html.H6(f"Дата: {data['time_now'][:10]}", className="card-subtitle mb-2 text-muted"),
            html.H6(f"Время: {data['time_now'][-5:]}", className="card-subtitle mb-2 text-muted"),
            html.Img(src=f"https:{data['icon']}", style={"height": "64px"}),
            html.H6(f"Температура: {data['temp']}°C", className="card-subtitle mb-2 text-muted"),
            html.P(f"{data['condition']}", className="card-text"),
        ], 
          className="card-information"
        )



        temp_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['temps'], mode='lines+markers', name='Температура')],
          # layout=go.Layout(title='Температура по часам', xaxis_title='Время', yaxis_title='Температура (°C)', template='plotly_dark') 
        )

        temp_fig.update_layout(
            title="Температура",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="часы",
            yaxis_title="Температура (°C)",
            font=dict(family="Roboto, sans-serif"),
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            # legend=dict(font=dict(size=st.GRAPH_FONT_SIZE),
            #             orientation='h',
            #             yanchor='bottom',
            #             y=1.02,
            #             xanchor='right',
            #             x=1),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,

        )


        ap_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['ap'], mode='lines+markers', name='Атмосферное давление')],
          # layout=go.Layout(title='Атмосферное давление по часам', xaxis_title='Время', yaxis_title='pa', template='plotly_dark') 
        )

        ap_fig.update_layout(
            title="Атмосферное давление",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Часы",
            yaxis_title="Давление (мбар)",
            font=dict(family="Roboto, sans-serif"),
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            # legend=dict(font=dict(size=st.GRAPH_FONT_SIZE),
            #             orientation='h',
            #             yanchor='bottom',
            #             y=1.02,
            #             xanchor='right',
            #             x=1),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,

        )

        co_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['co'], mode='lines+markers', name='Атмосферное давление')],
          # layout=go.Layout(title='Атмосферное давление по часам', xaxis_title='Время', yaxis_title='pa', template='plotly_dark') 
        )

        co_fig.update_layout(
            title="Точка росы",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Часы",
            yaxis_title="Температура (°C)",
            font=dict(family="Roboto, sans-serif"),
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            # legend=dict(font=dict(size=st.GRAPH_FONT_SIZE),
            #             orientation='h',
            #             yanchor='bottom',
            #             y=1.02,
            #             xanchor='right',
            #             x=1),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,

        )

        no2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm2_5'], mode='lines+markers', name='Атмосферное давление')],
          # layout=go.Layout(title='Атмосферное давление по часам', xaxis_title='Время', yaxis_title='pa', template='plotly_dark') 
        )

        no2_fig.update_layout(
            title="Влажность",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Часы",
            yaxis_title="Проценты (%)",
            font=dict(family="Roboto, sans-serif"),
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            # legend=dict(font=dict(size=st.GRAPH_FONT_SIZE),
            #             orientation='h',
            #             yanchor='bottom',
            #             y=1.02,
            #             xanchor='right',
            #             x=1),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,

        )

        o3_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['o3'], mode='lines+markers', name='Атмосферное давление')],
          # layout=go.Layout(title='Атмосферное давление по часам', xaxis_title='Время', yaxis_title='pa', template='plotly_dark') 
        )

        o3_fig.update_layout(
            title="Видимость",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Часы",
            yaxis_title="Расстояние (км)",
            font=dict(family="Roboto, sans-serif"),
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            # legend=dict(font=dict(size=st.GRAPH_FONT_SIZE),
            #             orientation='h',
            #             yanchor='bottom',
            #             y=1.02,
            #             xanchor='right',
            #             x=1),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,

        )


        so2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm10'], mode='lines+markers', name='Атмосферное давление')],
          # layout=go.Layout(title='Атмосферное давление по часам', xaxis_title='Время', yaxis_title='pa', template='plotly_dark') 
        )

        so2_fig.update_layout(
            title="Порывы ветра",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Часы",
            yaxis_title="Скорость (км/ч)",
            font=dict(family="Roboto, sans-serif"),
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            # legend=dict(font=dict(size=st.GRAPH_FONT_SIZE),
            #             orientation='h',
            #             yanchor='bottom',
            #             y=1.02,
            #             xanchor='right',
            #             x=1),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,

        )



       

      

        return weather_info, temp_fig, ap_fig, co_fig, no2_fig, o3_fig, so2_fig


'''
          weather_info = html.Div([
            html.H4(f"{data['city_name']}", className="card-title"),
            html.Img(src=f"https:{data['icon']}", style={"height": "64px"}),
            html.H5(f"{data['temp']}°C", className="card-subtitle mb-2 text-muted"),
            html.P(data['condition'], className="card-text")
        ])
'''