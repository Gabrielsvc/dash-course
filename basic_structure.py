# Estrutura básica: Imports
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Inicializar o app
app = dash.Dash(__name__)

# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
