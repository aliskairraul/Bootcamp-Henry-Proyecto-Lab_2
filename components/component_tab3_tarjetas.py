from dash import html
import polars as pl


def retorna_tarjetas_tab3(df: pl.DataFrame, accesos: int) -> tuple[html.Div, html.Div, html.Div]:
    """retorna_tarjetas_tab3: Retorna las 3 tarjetas del Tablero de la visualización

    Args:
        df (pl.DataFrame): Dataframe con la información de las primeras 2 tarjetas
        accesos (int): Información a Colocar en la Tercera Tarjeta

    Returns:
        tuple[html.Div, html.Div, html.Div]:
        html.Div: Tarjeta que muestra "Variacion Trimestral Acc 100 Hog"
        html.Div: Tarjeta que muestra "Variacion Trimestral MBPS"
        html.Div: Tarjeta que muestra "Total Accesos Trimestre"
    """
    tarjeta_1 = html.Div([
        html.Div(html.Label('Variación Trimestral Acc 100 Hog'), className='title_left'),
        html.Br(),
        html.Div(html.Label(f'{df["Crecimiento Accesos 100 Hog"][0]} %'), className='tarjetas')
    ], className='contenedor_tarjetas')

    tarjeta_2 = html.Div([
        html.Div(html.Label('Variación Trimestral MBPS'), className='title_left'),
        html.Br(),
        html.Div(html.Label(f'{df["Crecimineto MBPS Media Bajada"][0]} %'), className='tarjetas')
    ], className='contenedor_tarjetas')

    tarjeta_3 = html.Div([
        html.Div(html.Label('Total Accesos en Trimestre'), className='title_left'),
        html.Br(),
        html.Div(html.Label(f'{accesos:,}'), className='tarjetas')
    ], className='contenedor_tarjetas')

    return (tarjeta_1, tarjeta_2, tarjeta_3)
