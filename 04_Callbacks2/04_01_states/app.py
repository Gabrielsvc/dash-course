# Estrutura básica: Imports
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Inicializar o app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='in-1', type='text', value='Francisco'),
    dcc.Input(id='in-2', type='text' ,value='Gil'),
    html.Div(id='out-1'),
])

# Uso do input faz com que toda vez que uma propriedade seja alterada
# a função é chamada novamente e o valor é atualizado
# por vezes isso não é desejado (login por exemplo)

@app.callback(
    Output('out-1', "children"),
    Input('in-1', "value"),
    Input('in-2', "value"),
)
def update_output(in1, in2):
    return f'Quem te dá dor de cabeça é {in1} e {in2}'

# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
