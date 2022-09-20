from dash import Dash, dcc, html
import pandas as pd 
import plotly.express as px

app = Dash(__name__)

# ============================= Data

df = pd.DataFrame({ "Fruta":["banana", "maca", "uva", "banana", "maca", "uva"],
                    "Quantidade":[12, 7, 5, 22, 45, 94],
                    "Cidade": ['Montreal', 'Montreal', 'Montreal', 
                    'Nova Iorque', 'Nova Iorque', 'Nova Iorque']})
pop = pd.read_csv('populacao_estado_2011_2060.csv')

fig = px.line(pop, x='ano', y='projecao de populacao', color='estado',
              text='ano')
fig.update_traces(textposition="bottom right")
#fig = px.bar(df, x="Fruta", y="Quantidade", color="Cidade")

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
