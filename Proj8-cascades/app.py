# Estrutura básica: Imports
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

# Inicializar o app
app = dash.Dash(__name__)

all_options = {
    'Brasio': ['Natal', 'Jampa', 'Bom jesus da lapa'],
    'Deutschland': ['München', 'Bonn', 'Aachen']
}

app.layout = html.Div([
    dcc.RadioItems(
        list(all_options.keys()),
        'Deutschland',
        id='paises',
    ),

    html.Hr(),
    dcc.RadioItems(
        id='cidades'
    ),
    html.Hr(),
    html.Div(id='display')
])

@app.callback(
    Output('cidades', 'options'),
    Input('paises', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

@app.callback(
    Output('cidades', 'value'),
    Input('cidades', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('display', 'children'),
    Input('paises', 'value'),
    Input('cidades', 'value'))
def set_display_children(selected_country, selected_city):
    return f'{selected_city} is a city in {selected_country}'


# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
