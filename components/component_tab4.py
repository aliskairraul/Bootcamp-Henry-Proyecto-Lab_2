from dash import html
import plotly.express as px
import polars as pl
from components.component_tab4_left import component_tab4_left


df_accesos_localidades = pl.read_parquet('data/accesos_localidades_dash.parquet')


component_tab_4 = html.Div([
    html.Div([component_tab4_left], className='tab_subcontainers', id='tab4_left'),
    html.Div([], className='tab_subcontainers', id='tab4_center'),
    html.Div([], className='tab_subcontainers', id='tab4_right')
], className='work_container' , id='tab4_component')
