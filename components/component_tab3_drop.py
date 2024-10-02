from dash import html, dcc


def retorna_tab3_drop(periodos: list) -> html.Div:
    """retorna_tab3_drop: Retorna el componente Drop del Tablero

    Args:
        periodos (list): Lista de Periodos a desplegar en el Drop

    Returns:
        html.Div: Contenedor con el componente Drop
    """
    component_drop = html.Div([
        # html.Div(html.Label("Accesos Internet"), className='title_left'),
        html.Div(html.Label("Selecciona el Periodo (Trim)"), className='title_left'),
        html.Br(),
        html.Div([
            # html.Div(html.Label("Periodo"), id='label_periodo'),
            dcc.Dropdown(
                id="drop-tab3",
                options=periodos,
                value=periodos[0],
                style={
                    "backgroundColor": "#ffffff",
                    "fontSize": 18,
                    "color": "rgb(51, 51, 51)",
                    "border-radius": "1vh",
                },
            ),
        ], className='one_drop_tab4'),

    ], className='tab_left')
    return component_drop
