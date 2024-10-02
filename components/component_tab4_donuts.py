import polars as pl
import plotly.graph_objects as go
from dash import html, dcc


def retorna_graf_tab4(df_pie_rangos: pl.DataFrame, df_tecnologias: pl.DataFrame) -> html.Div:
    """retorna_graf_tab4: Retorna el contenedor que contiene los Gráficos tipo Tortas de la pestaña
                          que muestra el Mapa en la visualizació
    Args:
        df_pie_rangos (pl.DataFrame): Dataframe con la data para el gráfico de Rangos de Velocidades
        df_tecnologias (pl.DataFrame): Dataframe con la data pata el gráfico de las tecnologías

    Returns:
        html.Div: contenedor con los gráficos tipo torta
    """
    # Convertir columnas a listas de valores
    valores_pie_rangos = [df_pie_rangos[0, i] for i in range(len(df_pie_rangos.columns))]
    valores_tecnologias = [df_tecnologias[0, i] for i in range(len(df_tecnologias.columns))]

    # Crear gráfico Donut para df_pie_rangos
    fig_rangos = go.Figure(go.Pie(
        labels=df_pie_rangos.columns,
        values=valores_pie_rangos,
        marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA']),
        legendgroup='rangos',
        hoverlabel=dict(
            font_size=16,
            font_color="black",
        )
    ))

    fig_rangos.update_layout(
        font=dict(color='#ffffff', size=16),
        paper_bgcolor='rgba(0,0,0,0)',
        height=270,
        margin=dict(t=0, b=0, l=0, r=0),
        legend=dict(
            title='Rangos',
            yanchor="top",
            y=0.7,
            xanchor="left",
            x=0.9,
            traceorder='normal'
        )
    )

    # Crear gráfico Donut para df_tecnologias
    fig_tecnologias = go.Figure(go.Pie(
        labels=df_tecnologias.columns,
        values=valores_tecnologias,
        marker=dict(colors=['#FFA15A', '#19D3F3', '#FF6692', '#B6E880']),
        legendgroup='tecnologias',
        hoverlabel=dict(
            font_size=16,
            font_color="black",
        )
    ))

    fig_tecnologias.update_layout(
        font=dict(color='#ffffff', size=16),
        paper_bgcolor='rgba(0,0,0,0)',
        height=270,
        margin=dict(t=0, b=0, l=0, r=0),
        legend=dict(
            title="Tecnologías",
            yanchor="top",
            y=0.7,
            xanchor="left",
            x=1.0,
            traceorder='normal'
        )
    )

    config = {'displayModeBar': False}

    # Crear los componentes dcc.Graph dentro de un html.Div
    componente_graf_tab4 = html.Div([
        html.Label("Accesos por Rangos de Velocidad y tecnologías", className='title_left'),
        html.Br(),
        html.Br(),
        html.Br(),
        dcc.Graph(figure=fig_rangos, config=config),
        html.Br(),
        dcc.Graph(figure=fig_tecnologias, config=config)
    ], id='contenedor_pies_tab4')

    return componente_graf_tab4
