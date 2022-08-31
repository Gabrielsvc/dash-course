# Estrutura básica: Imports
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import numpy as np


# Inicializar o app
app = dash.Dash(__name__)

# ==================== Layout ==================== #
app.layout = html.Div(children=[

    ]
)

# ==================== Callbacks ==================== #



# ==================== Run server ==================== #
if __name__ == '__main__':
    app.run_server(debug=True)
