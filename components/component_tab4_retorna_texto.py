from dash import html


def retorna_tab4_texto_resultado(
        total_poblacion: int, total_localidades: int, total_accesos: int
) -> html.Div:
    """retorna_tab4_texto_resultado: Retorna la informacion tipo texto que se muestra en la parte
                                     izquierda en la pestaña del mapa

    Args:
        total_poblacion (int): Número de habitantes en el Rango de habitantes escogido
        total_localidades (int): Número de localidades en el Rango de habitantes escogido
        total_accesos (int): Número de accesos a internet en el Rango de habitantes escogido

    Returns:
        html.Div: Contenedor con la Información tipo texto mostrada en la pestaña del Mapa
    """
    accesos_100_hab = round(100 * (total_accesos / total_poblacion), 2)
    component = html.Div([
        html.Div(html.Label('Datos de Valor'), className='title_left'),
        html.Br(),
        html.Label('Localidades del Rango'),
        html.Br(),
        html.Label(f"{total_localidades:,}"),
        html.Br(),
        html.Br(),
        html.Label('Población del Rango'),
        html.Br(),
        html.Label(f"{total_poblacion:,}"),
        html.Br(),
        html.Br(),
        html.Label('Total Accesos en Rango'),
        html.Br(),
        html.Label(f"{total_accesos:,}"),
        html.Br(),
        html.Br(),
        html.Label('Accesos Cada 100 Hab'),
        html.Br(),
        html.Label(accesos_100_hab)
    ], id='texto_tab4')
    return component
