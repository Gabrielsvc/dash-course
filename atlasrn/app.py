# Estrutura básica: Imports
import dash
import os
import pandas as pd
import plotly.graph_objects as go

from dash import html, dcc
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots


# TODO All simulated towers have the same value??

# Dash app com Figure e Slider
def get_obs_data():
    obs_folder='/home/gsvc/Repos/atlas-rn/Simulação-RN/dados_observados/'
    files=sorted(os.listdir(obs_folder))
    ms01, ms02, ms03, ms05=files
    tower_names=['ms01', 'ms02', 'ms03', 'ms05']

    df_ms01=pd.read_csv(obs_folder+ms01, sep='\t', skiprows=11,
                        decimal=',',encoding='unicode_escape') 
    df_ms02=pd.read_csv(obs_folder+ms02, sep='\t', skiprows=11,
                        decimal=',',encoding='unicode_escape') 
    df_ms03=pd.read_csv(obs_folder+ms03, sep='\t', skiprows=11,
                        decimal=',',encoding='unicode_escape') 
    df_ms05=pd.read_csv(obs_folder+ms05, sep='\t', skiprows=11,
                        decimal=',',encoding='unicode_escape')
    
    df_list=[df_ms01, df_ms02, df_ms03, df_ms05]

    df_obs = pd.concat(
        [df.assign(tower=tower) for df, tower in zip(df_list, tower_names)])
    return df_obs


def get_sim_data(month):
    sim_folder=f'/home/gsvc/Repos/atlas-rn/Simulação-RN/dados_simulados/'
    for folder in os.listdir(sim_folder):
        if folder.startswith(month):
            sim_folder=sim_folder+folder+'/'
            break

    li =[]
    dfs = []
    for tower in sorted(os.listdir(sim_folder)):
        folder = sim_folder+tower+'/'
        for file in sorted(os.listdir(folder)):
            df = pd.read_csv(folder+file, sep=';')
            li.append(df)
        dfs.append(li)
        li = []

    tower_names=['ms01', 'ms02', 'ms03', 'ms05']

    df_ms01=pd.concat(dfs[0], axis=0, ignore_index=True)
    df_ms02=pd.concat(dfs[1], axis=0, ignore_index=True)
    df_ms03=pd.concat(dfs[2], axis=0, ignore_index=True)
    df_ms05=pd.concat(dfs[3], axis=0, ignore_index=True)
    df_list=[df_ms01, df_ms02, df_ms03, df_ms05]

    df_sims = pd.concat(
        [df.assign(tower=tower) for df, tower in zip(df_list, tower_names)])
    return df_sims


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Inicializar o app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df_sims = get_sim_data('01')
fig = make_subplots(rows=2, cols=2, subplot_titles=('ms-01', 'ms-02', 'ms-03',
'ms-05'))

fig.append_trace(go.Scatter(x=df_sims['data'].loc[df_sims['tower']== 'ms01'], y=df_sims['value'], mode='lines+markers'), row=1, col=1)
fig.append_trace(go.Scatter(x=df_sims['data'].loc[df_sims['tower']== 'ms02'],
y=df_sims['value'].loc[df_sims['tower']=='ms02'], mode='lines+markers'), row=2, col=1)
fig.append_trace(go.Scatter(x=df_sims['data'].loc[df_sims['tower']== 'ms03'],
y=df_sims['value'].loc[df_sims['tower']=='ms03'], mode='lines+markers'), row=1,
col=2)
fig.append_trace(go.Scatter(x=df_sims['data'].loc[df_sims['tower']== 'ms05'],
y=df_sims['value'].loc[df_sims['tower']=='ms05'], mode='lines+markers'), row=2,
col=2)

'''
fig1 = px.scatter(df_sims.loc[df_sims['tower'] == 'ms01'], x='data', y='value',
line_color='#ffe476', mode='lines+markers')
fig2 = px.scatter(df_sims.loc[df_sims['tower'] == 'ms02'], x='data', y='value',
line_color='#88e746', mode='lines+markers')
fig3 = px.scatter(df_sims.loc[df_sims['tower'] == 'ms03'], x='data', y='value', color='tower')
fig5 = px.scatter(df_sims.loc[df_sims['tower'] == 'ms05'], x='data', y='value', color='tower')
'''
app.layout = html.Div([
    dcc.Graph(id='graph-ms01', figure=fig, style={'height':'100vh', 'width':
    '200vh'})
])

'''
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.date == selected_year]
    
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop',
                     color='continent', hover_name='country', log_x=True,
                     size_max=55)

    fig.update_layout(transition_duration=1000)
    return fig
'''


# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
