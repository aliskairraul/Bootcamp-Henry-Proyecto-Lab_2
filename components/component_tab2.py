from dash import html
from components.component_tab2_left import component_tab2_left


component_tab_2 = html.Div([
    html.Div([component_tab2_left], className='tab_subcontainers', id='tab2_left'),
    html.Div([
        html.Div([], id='title_right_tab2'),
        html.Div([], id='grafico_right_tab2'),
    ], className='tab_subcontainers', id='tab2_right')
], className='work_container', id='tab2_component')
