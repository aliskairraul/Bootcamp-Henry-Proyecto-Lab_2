from dash import html

componente_1 = html.Div([
    html.Div(html.Label('Importante Analizar'), className='title_left'),
    html.Br(),
    html.Div([
        html.P([
            'Desde el Año ',
            html.B('2018'),
            ' al ',
            html.B('2024'),
            ' se observa un aumento superior a ',
            html.B('1000 %'),
            ' !!!'
        ], style={
            'text-indent': '1.5rem',  # Sangría del párrafo
            'line-height': '1.6',    # Espacio de interlineado
            'text-align': 'justify',  # Justificado
            'font-size': '1.1rem'      # Tamaño de la letra
        })
    ], className='parrafo_left')
])

componente_2 = html.Div([
    html.Div(html.Label('Analizando lo Observado'), className='title_left'),
    html.Br(),
    html.Div([
        html.P([
            'Escenario de Inflación y/o Devaluación Local',
        ], style={
            'text-indent': '1.5rem',  # Sangría del párrafo
            'line-height': '1.6',    # Espacio de interlineado
            'text-align': 'justify',  # Justificado
            'font-size': '1.1rem'      # Tamaño de la letra
        })
    ], className='parrafo_left')
])

componente_3 = html.Div([
    html.Div(html.Label('Analizando lo Observado'), className='title_left'),
    html.Br(),
    html.Div([
        html.P([
            'Ingresos de 2024 representan ',
            html.B('48.79 %'),
            ' con respecto a 2014'
        ], style={
            'text-indent': '1.5rem',  # Sangría del párrafo
            'line-height': '1.6',    # Espacio de interlineado
            'text-align': 'justify',  # Justificado
            'font-size': '1.1rem'      # Tamaño de la letra
        })
    ], className='parrafo_left')
])

componente_4 = html.Div([
    html.Div(html.Label('Analizando lo Observado'), className='title_left'),
    html.Br(),
    html.Div([
        html.P([
            'Claramente Internet es la única Tecnología que aumento su ',
            'penetración de Mercado'
        ], style={
            'text-indent': '1.5rem',  # Sangría del párrafo
            'line-height': '1.6',    # Espacio de interlineado
            'text-align': 'justify',  # Justificado
            'font-size': '1.1rem'      # Tamaño de la letra
        })
    ], className='parrafo_left')
])

componente_7 = html.Div([
    html.Div(html.Label('Analizando lo Observado'), className='title_left'),
    html.Br(),
    html.Div([
        html.P([
            'A pesar de la caida de minutos consumidos y llamadas realizadas los ',
            'accesos a la Telefonía Móvil han variado MUY POCO'
        ], style={
            'text-indent': '1.5rem',  # Sangría del párrafo
            'line-height': '1.6',    # Espacio de interlineado
            'text-align': 'justify',  # Justificado
            'font-size': '1.1rem'      # Tamaño de la letra
        })
    ], className='parrafo_left')
])


componente_8 = html.Div([
    html.Div(html.Label('Queda Muy Claro !!!'), className='title_left'),
    html.Br(),
    html.Div([
        html.P([
            'EL Internet es la Tecnología de Telecomunicaciones con mayor avance ',
            'de penetración en la última Decada'
        ], style={
            'text-indent': '1.5rem',  # Sangría del párrafo
            'line-height': '1.6',    # Espacio de interlineado
            'text-align': 'justify',  # Justificado
            'font-size': '1.1rem'      # Tamaño de la letra
        })
    ], className='parrafo_left')
])

componente_9 = html.Div([
    html.Div(html.Label('A tener en Cuenta !!!'), className='title_left'),
    html.Br(),
    html.Div([
        html.P([
            'A pesar de que los Accesos a Internet han venido creciendo con el tiempo ',
            'se observan tipos de tecnologías para acceder a ella, que vienen en declive'
        ], style={
            'text-indent': '1.5rem',  # Sangría del párrafo
            'line-height': '1.6',    # Espacio de interlineado
            'text-align': 'justify',  # Justificado
            'font-size': '1.1rem'      # Tamaño de la letra
        })
    ], className='parrafo_left')
])


componente_10 = html.Div([
    html.Div(html.Label('Acá puede haber una Oportunidad'), className='title_left'),
    html.Br(),
    html.Div([
        html.P([
            'Es claro que la población desea migrar a servicios de Internet, que les ofrezcan ',
            'una conexión de mayor velocidad, por eso la migración hacia FIBRA OPTICA y CABLEMODEM, ',
            'en deprimento de ADSL y WIFI'
        ], style={
            'text-indent': '1.5rem',  # Sangría del párrafo
            'line-height': '1.6',    # Espacio de interlineado
            'text-align': 'justify',  # Justificado
            'font-size': '1.1rem'      # Tamaño de la letra
        }),
        html.Br(),
        html.P([
            'PEEERO y en aquellas Localidades donde la Densidad de Población No Justifique un Cableado ??? ',
        ], style={
            'text-indent': '1.5rem',  # Sangría del párrafo
            'line-height': '1.6',    # Espacio de interlineado
            'text-align': 'justify',  # Justificado
            'font-size': '1.1rem'      # Tamaño de la letra
        }),
    ], className='parrafo_left')
])


textos_left_tab2 = [
    componente_1,
    componente_2,
    componente_3,
    componente_4,
    None,
    None,
    componente_7,
    componente_8,
    componente_9,
    componente_10
]
