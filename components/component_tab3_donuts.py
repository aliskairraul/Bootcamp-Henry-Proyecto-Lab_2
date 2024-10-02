import polars as pl
import plotly.graph_objects as go
from dash import html, dcc


def retorna_pies_tab3(df: pl.DataFrame) -> html.Div:
    """retorna_pies_tab3: Retorna los Graficos tipo torta del Tablero

    Args:
        df (pl.DataFrame): Dataframe con la data para generar los gráficos

    Returns:
        html.Div: Contenedor con los Gráficos tipo barra
    """
    valores_pie_rangos = [df['Hasta 10 Mbps'].sum(), df['10.01 - 30 Mbps'].sum(),
                          df['30.01 - 100 Mbps'].sum(), df['Mayor a 100 Mbps'].sum()]
    valores_tecnologias = [df['ADSL'].sum(), df['CABLEMODEM'].sum(), df['FIBRA'].sum(), df['WIRELESS'].sum()]

    # Crear gráfico Donut para rangos
    fig_rangos = go.Figure(go.Pie(
        labels=['Hasta 10 Mbps', '10.01 - 30 Mbps', '30.01 - 100 Mbps', 'Mayor a 100 Mbps'],
        values=valores_pie_rangos,
        marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA']),
        legendgroup='rangos',
        hoverlabel=dict(
            font_size=16,
            font_color="black",
        )
    ))

    fig_rangos.update_layout(
        font=dict(color='#ffffff', size=14),
        paper_bgcolor='rgba(0,0,0,0)',
        height=230,
        margin=dict(t=20, b=0, l=0, r=20),
        legend=dict(
            title="Rangos",
            yanchor="top",
            y=0.9,
            xanchor="left",
            x=1.0,
            traceorder='normal'
        )
    )

    # Crear gráfico Donut para tecnologias
    fig_tecnologias = go.Figure(go.Pie(
        labels=['ADSL', 'CABLEMODEM', 'FIBRA', 'WIRELESS'],
        values=valores_tecnologias,
        marker=dict(colors=['#FFA15A', '#19D3F3', '#FF6692', '#B6E880']),
        legendgroup='tecnologias',
        hoverlabel=dict(
            font_size=16,
            font_color="black",
        )
    ))

    fig_tecnologias.update_layout(
        font=dict(color='#ffffff', size=14),
        paper_bgcolor='rgba(0,0,0,0)',
        height=230,
        margin=dict(t=0, b=0, l=0, r=20),
        legend=dict(
            title="Tecnologías",
            yanchor="top",
            y=0.9,
            xanchor="left",
            x=1.0,
            traceorder='normal'
        )
    )

    config = {'displayModeBar': False}

    # Crear los componentes dcc.Graph dentro de un html.Div
    componente_graf_tab3 = html.Div([
        html.Label("Accesos por Rangos de Velocidad y tecnologías", className='title_left'),
        dcc.Graph(figure=fig_rangos, config=config),
        html.Br(),
        html.Br(),
        dcc.Graph(figure=fig_tecnologias, config=config)
    ])

    return componente_graf_tab3
