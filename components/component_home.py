from dash import html

component_home = html.Div([
    html.Div([
        html.Div([
            html.Div(html.Label("Telecomunicaciones Argentina"), id='title_home'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Ul([
                html.Li([
                    "¿Porqué Internet?:",
                    html.Ul([
                        html.Li("Análisis del comportamiento de las Distintas Tecnologías de Telecomunicación")
                    ], className='textos_pestanas')
                ], id="contexto", className="pestanas"),
                html.Br(),
                html.Br(),
                html.Li([
                    "Seguimiento a Métricas:",
                    html.Ul([
                        html.Li("Seguimiento a los Indicadores de Gestión Trimestrales del Internet")
                    ], className='textos_pestanas')
                ], id="tablero", className="pestanas"),
                html.Br(),
                html.Br(),
                html.Li([
                    "Mapa de Oportunidades:",
                    html.Ul([
                        html.Li("Mapa de seguimiento de Oportunidades por Rangos de Población")
                    ], className='textos_pestanas')
                ], id="mapa", className="pestanas")
            ])

        ], className="home-content"),
    ], id='tab_home'),
], className='work_container', id='tab2_component')
