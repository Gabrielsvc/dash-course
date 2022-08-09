# Estrutura básica: Imports
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Inicializar o app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Altere o valor abaixo para ver o callback em ação!"),
    html.Div(["Entrada:",
        dcc.Input(id='my-input', value='Valor inicial', type='text')]),
    html.Br(),
    html.Div(id='my-output'),
])

@app.callback(
    [], [], []
)
def update_output_div(value):
    return "Saída: {}".format(value)


# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
