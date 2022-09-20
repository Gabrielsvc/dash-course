import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__)
server = app.server
# ========================= Data ============================= #
suma = pd.read_csv('supermarket_sales.csv')
# suma.info shows info on each column
suma['Date'] = pd.to_datetime(suma['Date'])


# ========================== Layout ========================== #
app.layout = html.Div(children=[
        html.H3("Cidades: "),
        #dcc.Dropdown(suma['City'].unique(), suma['City'].unique(),
        #             multi=True, id='drop_city'),
        dcc.Checklist(suma["City"].value_counts().index,
                      suma["City"].value_counts().index, id="check_city"),
        html.H3('Variável de Análise: '),
        dcc.RadioItems(['gross income', 'Rating'], 'Rating', id='main_variable'),
        dcc.Graph(id='city_fig'),
        dcc.Graph(id='pay_fig'),
        dcc.Graph(id='income_per_product_fig'),
    ]
)

# ========================= Callbacks ======================== #
# Lista de outputs e inputs
@app.callback([
    Output('city_fig', 'figure'),
    Output('pay_fig', 'figure'),
    Output('income_per_product_fig', 'figure'),
    ],[
    Input('check_city', 'value'),
    Input('main_variable', 'value')
    ]
)
def render_graphs(cities, main_variable):
    # Somamos todos os valores para lucro e tomamos média para rating
    operation = np.sum if main_variable == "gross income" else np.mean
    df_filtered =  suma[suma['City'].isin(cities)]

    df_city = (df_filtered.groupby("City")[main_variable].
                apply(operation).
                to_frame().
                reset_index())
    df_payment = (df_filtered.groupby('Payment')[main_variable].
                  apply(operation).
                  to_frame().
                  reset_index())
    df_prod_inc = (df_filtered.groupby(['Product line', 'City'])[main_variable].
                  apply(operation).
                  to_frame().
                  reset_index())

    fig_city = px.bar(df_city, x="City", y=main_variable)
    fig_payment = px.bar(df_payment, x=main_variable, y='Payment', orientation='h')
    fig_prod_inc = px.bar(df_prod_inc, x=main_variable,
                          y='Product line', color='City', orientation='h')

    fig_city.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=200)
    fig_payment.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=200)
    fig_prod_inc.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=600)


    return fig_city, fig_payment, fig_prod_inc


# ========================= Server run ======================= #
if __name__ == '__main__':
        app.run_server(port=8051, debug= True)
