from dash import html
import dash_daq as daq

component_tab2_left = html.Div([
    html.Div(html.Label("Tendencias Tecnologías"), className='title_left'),
    html.Br(),
    html.Br(),
    html.Div([
        html.Label("Diapositiva Número "),
        daq.NumericInput(
            id='control_slides_tab2',
            value=0,
            min=0,
            max=10,
            size=60,
            style={'backgroundColor': '#f0f0f0'}  # Cambia el color de fondo aquí
        ),
    ], id='container_control_slides'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(id='texto_tab2')
])
