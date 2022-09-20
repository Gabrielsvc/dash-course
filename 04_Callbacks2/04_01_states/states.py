# Estrutura básica: Imports
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

# Inicializar o app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='in-1', type='text', value='Francisco'),
    dcc.Input(id='in-2', type='text' ,value='Gil'),
    html.Button(id='btn-1', children='Submit'),
    html.Div(id='out-1'),
])

@app.callback(
    Output('out-1', "children"),
    Input('btn-1', 'n_clicks'),
    State('in-1', "value"),
    State('in-2', "value"),
)
def update_output(clicks, in1, in2):
    return f'Quem te dá dor de cabeça é {in1} e {in2}'

# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
