import plotly.express as px
from dash import dcc, html
import polars as pl
import pandas as pd


def retorna_barras_tab3(df: pl.DataFrame) -> html.Div:
    """retorna_barras_tab3: Retorna el Grafico de Barras que se muestra en el Tablero

    Args:
        df (pl.DataFrame): Dataframe con los datos necesarios para realizar el Gráfico

    Returns:
        html.Div: Contenedor con el Grafico de Barras
    """
    df = df.to_pandas()

    df_grouped = df.melt(id_vars='Provincia',
                         value_vars=['Accesos 100 Hog', 'MBPS Media Bajada'],
                         var_name='Metrica',
                         value_name='Valor')

    df_grouped = pd.merge(df_grouped, df[['Provincia', 'Accesos 100 Hog Anterior', 'KPI 100 Hog',
                                          'Cumplimineto KPI 100 Hog', 'Crecimiento Trimestral Accesos 100 Hog',
                                          'MBPS Anterior', 'KPI MBPS', 'Cumplimineto KPI MBPS',
                                          'Crecimiento Trimestral MBPS', 'Accesos 100 Hog', 'MBPS Media Bajada']],
                          on='Provincia', how='left')

    fig = px.bar(df_grouped, x='Provincia', y='Valor', color='Metrica', barmode='group',
                 custom_data=df_grouped)

    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>Provincia: %{customdata[0]}</b>",
            "Accesos 100 Hog del Trimestre: %{customdata[11]}",
            "MBPS del Trimestre: %{customdata[12]}",
            "</br>"
            "<b>KPI Accesos 100 Hog: Crecimiento Trimestral 2%</b>",
            "Valor Anterior: %{customdata[3]}",
            "<b>Objetivo KPI: %{customdata[4]}</b>",
            "<b>Cumplimiento KPI: %{customdata[5]} %</b>",
            "Crecimiento Trimestral: %{customdata[6]} %",
            "<br>"
            "<b>KPI MBPS: Crecimiento Trimestral 5%</b>",
            "Valor Anterior: %{customdata[7]}",
            "<b>Objetivo KPI: %{customdata[8]}</b>",
            "<b>Cumplimiento KPI: %{customdata[9]} % </b>",
            "Crecimiento Trimestral: %{customdata[10]} %",
        ]),
        hoverlabel=dict(bgcolor="white", font_color="black", font_size=16),
        width=0.4,
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Accesos",
        font=dict(color='#ffffff', size=14),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=True, linecolor='#ffffff', tickangle=-90),
        yaxis=dict(showgrid=False, zeroline=True, linecolor='#ffffff'),
        legend=dict(
            x=0.8,
            y=1.1,
            orientation='v'
        )
    )
    componente = html.Div([
        html.Label("Accesos a Internet por cada 100 Hogares y Velocidad Media de Bajada", className='title_left'),
        html.Br(),
        dcc.Graph(figure=fig, config={'displayModeBar': False}),
        html.Label("Nota: Los KPIs por PROVINCIA se muestran en los ToolTips", id='pie_pagina_tab3')
    ], style={'width': '100%', 'height': '80%'}, id='grafico_barras_tab3')
    return componente
