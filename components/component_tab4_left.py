from dash import html, dcc


minimos = [2000, 5000, 10000, 20000, 50000, 100000, 500000]
maximos = [5000, 10000, 20000, 50000, 100000, 500000, 3000000]


component_tab4_left = html.Div([
    dcc.Store(id="store_tab4", data={"btn_tab4": 0}),
    html.Div(html.Label("Rango Habitantes"), className='title_left'),
    html.Br(),
    html.Div([
        html.Label("Minimo"),
        dcc.Dropdown(
            id="drop-minimo_tab4",
            options=minimos,
            value=minimos[0],
            style={
                "backgroundColor": "#ffffff",
                "fontSize": 14,
                "color": "rgb(51, 51, 51)",
                "border-radius": "1vh",
            },
        ),
    ], className='one_drop_tab4'),
    html.Br(),
    html.Div([
        html.Label("Máximo"),
        dcc.Dropdown(
            id="drop-maximo_tab4",
            options=maximos,
            value=maximos[0],
            style={
                # "backgroundColor": "#70cbff",
                "backgroundColor": "#ffffff",
                "fontSize": 14,
                "color": "rgb(51, 51, 51)",
                "border-radius": "1vh",
            },
        ),
    ], className='one_drop_tab4'),
    html.Br(),
    html.Br(),
    html.Div(
        html.Button("Ok", className="btns", id="btn_tab4"),
        className="btn-container",
        id="btn_container_tab4",
    ),
    html.Br(),
    html.Div([], id='tab4_rangos_response'),
    html.Br(),
    # html.Br(),
    html.Div([], id='tab4_texto_resultados')
], className='tab_left')
