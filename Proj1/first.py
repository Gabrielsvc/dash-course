from dash import Dash, dcc, html
import pandas as pd 
import plotly.express as px

app = Dash(__name__)

# ============================= Data
df = pd.DataFrame({ "Fruta":["banana", "maca", "uva"],
                    "Quantidade":[12, 7, 5],
                    "Preco": [2.34, 5.63, 1.70]})

fig = px.bar(df, x="Fruta", y="Quantidade", color="Preco")

# ============================= Layout

app.layout = html.Div(id="d1",
    children = [
            html.H1("Hello Dash",id="h1"),
            html.Div("Dash: um Framework para python"),
            dcc.Graph(figure=fig)
    ]
)

if __name__=='__main__':
    app.run_server(debug=True)