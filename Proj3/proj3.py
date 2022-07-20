# Estrutura básica: Imports
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Inicializar o app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label("Dropdown"),

    dcc.Dropdown(
        id='dp-1',
        options=[{'label':'Rio Grande do Sul', 'value':'RS'},
        {'label':'Sao Paulo', 'value':'SP'},
        {'label':'Minas Gerais', 'value':'MG'}],
        value="MG",
        style={"margin-bottom":"25px"}
    ),
    html.Label("Checklist",style={"margin-top":"50px"}),

    dcc.Checklist(
        id='dl-1',
        options=[{'label':'Rio Grande do Sul', 'value':'RS'},
        {'label':'Sao Paulo', 'value':'SP'},
        {'label':'Minas Gerais', 'value':'MG'}],
        value=["MG"],
        style={"margin-bottom":"25px"}
    ),
    html.Label('Text Input'),
    dcc.Input(value='SP', type='text'),

    html.Label('Slider'),
    dcc.Slider(min=0,
        max=10,
        marks={i: str(i) for i in range(2,9)},
        value=5),
        
    html.Div(id='dd-output-container')
])

# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
