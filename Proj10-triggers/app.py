# Estrutura básica: Imports
import dash
from dash import html, dcc, Input, Output, callback_context

# Inicializar o app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Button 1', id='btn1'),
    html.Button('Button 2', id='btn2'),
    html.Button('Button 3', id='btn3'),
    html.Div(id='ctn-example')
])


@app.callback(Output('ctn-example', 'children'),
              Input('btn1', 'n_clicks'),
              Input('btn2', 'n_clicks'),
              Input('btn3', 'n_clicks'))
def display(btn1, btn2, btn3):
    id_triggered = callback_context.triggered[0]['prop_id'].split('.')[0]
    return id_triggered

# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
