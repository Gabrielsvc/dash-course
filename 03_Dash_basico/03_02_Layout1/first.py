import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

#  Formas de alterar estilos 
# 1 - definir um stylesheet
# 2 - adicionar um .css na pasta assets
# 3 - inserir um atributo style como um dicionário
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(id="d1",
    children = [
            html.H1("Hello Dash",id="h1", style={"color":"#F5F002"}),
            html.Div("Dash: um Framework para python"),
    ]
)

if __name__=='__main__':
    app.run_server(debug=True)