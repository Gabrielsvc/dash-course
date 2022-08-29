# Estrutura básica: Imports
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd

# Inicializar o app
app = Dash(__name__)

df = pd.DataFrame({'student_id': np.arange(1,11),
                   'score' : np.random.randint(1,10, 10)
                 })

app.layout = html.Div([
    dcc.Dropdown(list(range(1, 11)), 1, id='score'),
    'Foi pontuado pela seguinte quantidade de estudantes: ',
    html.Div(id='output'),
    dcc.Store(id='store'),
])


@app.callback(Output('store', 'data'),
              Input('score', 'value'))
def update_output(value):
    # Operação custosa
    filtered_df = df[df['score'] == value]
    # ... 
    return filtered_df.to_dict()


@app.callback(Output('output', 'children'),
              Input('store', 'data'))
def update_output(data):
    filtered_df = pd.DataFrame(data)
    return len(filtered_df)


# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)