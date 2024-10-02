import polars as pl
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def retorna_pies_eda_internet(df: pl.DataFrame, periodo: str) -> tuple[go.fig, go.fig]:
    """retorna_pies_eda_internet: retorna los gráficos de Torta para el archivo 05_eda_internet.ipynb

    Args:
        df (pl.DataFrame): Dataframe con la data a graficar
        periodo (str): Periodo estudiado. Solo para Uso en titulos de los Gráficos

    Returns:
        tuple[go.fig, go.fig]: Dos Gráfico de Torta de la libreria Plotly
    """
    valores_pie_rangos = [df['Hasta 10 Mbps'].sum(), df['10.01 - 30 Mbps'].sum(),
                          df['30.01 - 100 Mbps'].sum(), df['Mayor a 100 Mbps'].sum()]
    valores_tecnologias = [df['ADSL'].sum(), df['CABLEMODEM'].sum(), df['FIBRA'].sum(), df['WIRELESS'].sum()]

    # Pie para rangos
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
        title=f'Distribución de los accesos de Internet según Rangos de Velocidad   ({periodo})',
        font=dict(color='black', size=14),
        height=230,
        margin=dict(t=50, b=0, l=0, r=0),
        legend=dict(
            title="Rangos",
            yanchor="top",
            y=0.9,
            xanchor="left",
            x=1.0,
            traceorder='normal'
        )
    )

    # Pie para tecnologias
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
        title=f'Distribución de los accesos de Internet según Tecnologías  ({periodo})',
        font=dict(color='black', size=14),
        height=230,
        margin=dict(t=50, b=0, l=0, r=0),
        legend=dict(
            title="Tecnologías",
            yanchor="top",
            y=0.9,
            xanchor="left",
            x=1.0,
            traceorder='normal'
        )
    )
    return fig_rangos, fig_tecnologias


def retorna_barras_eda_05(df: pl.DataFrame, periodo: str) -> px.fig:
    """retorna_barras_eda_05: Retorna los gráfico de Barras en el archivo 05_eda_internet.ipynb

    Args:
        df (pl.DataFrame): Dataframe con la data a graficar
        periodo (str): Periodo estudiado. Solo para Uso en titulo del Gráfico

    Returns:
        px.fig: Gráfico de Barras de Plotly express
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
        title=f"Accesos 100 Hog y MBPS por Provincia en el periodo  ({periodo})",
        xaxis_title="",
        yaxis_title="Accesos",
        font=dict(color='black', size=14),
        xaxis=dict(showgrid=False, zeroline=True, linecolor='black', tickangle=-90),
        yaxis=dict(showgrid=False, zeroline=True, linecolor='black'),
        legend=dict(
            x=0.8,
            y=1.1,
            orientation='v'
        )
    )
    return fig
