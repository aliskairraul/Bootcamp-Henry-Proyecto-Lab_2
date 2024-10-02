import polars as pl
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

internet_pais = pl.read_parquet('data/internet_tab2.parquet')
telefonia_movil = pl.read_parquet('data/telefonia_movil_tab2.parquet')
telefonia_fija = pl.read_parquet('data/telefonia_fija_tab2.parquet')
television = pl.read_parquet('data/television_tab2.parquet')
df_pies = pl.read_parquet('data/df_pie_tab2.parquet')
tecnologias_grafico_9 = pl.read_parquet('data/tecnologias_internet_graficos_tab2.parquet')
rangos_grafico_10 = pl.read_parquet('data/rangos_internet_graficos_tab2.parquet')

# Listas de Dataframes, Nombres de Graficos y Colores Para los Gráficos con 4 Lineas
dfs_4 = [internet_pais, telefonia_movil, telefonia_fija, television]
list_4 = ["Internet", "Telefonía Móvil", "Telefonía Fija", "Televisión"]
colors_4 = ['#22D3EE', '#38C172', '#F6993F', '#FFED4A']


# Listas de Datagrames, Nombres de Graficos y Colores Para los Gráficos con 3 Lineas
dfs_3 = [internet_pais, telefonia_fija, television]
list_3 = ["Internet", "Telefonía Fija", "Televisión"]
colors_3 = ['#22D3EE', '#F6993F', '#FFED4A']


# ESTA FUNCION CREA LAS GRAFICAS 1, 2 y 4 del Tab 2
def crear_grafica(df_list: list, y_column: str, list_names: list, colors: list) -> px.line:
    """Crear gráfica: Función para crear gráficas de tendencias

    Args:
        df_list (list): Lista de Dataframes
        y_column (str): Columna del dataframe a graficar
        title (str): Título del gráfico
        list_names (list): Lista de Nombres de los gráficos
        colors (list): Lista de Colores

    Returns:
        px.line: Grafica de linea de la Libreria plotly
    """
    fig = px.line()
    # Aca esto es como 3 ciclos for en paralelo cada variable
    for df, name, color in zip(df_list, list_names, colors):
        fig.add_scatter(x=df["fecha"], y=df[y_column], mode='lines', name=name, line=dict(color=color))

    fig.update_layout(
        xaxis_title='Periodo',
        yaxis_title=y_column,
        font=dict(color='#ffffff', size=16),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',  # Fondo de la grilla transparente
        xaxis=dict(showgrid=False, zeroline=True, linecolor='#ffffff'),
        yaxis=dict(showgrid=False, zeroline=True, linecolor='#ffffff'),
        height=600,
    )
    return fig


# ESTA SOLO HACE EL GRAFICO DE TORTAS DEL TAB 2
def crear_graf_pie(df: pl.DataFrame, colors: list):
    """crear_graf_pie: Crea un Subplot de Pies de Plotly. Muestran la comparación
                       de ingresos en Dolares entre 2014 y 2024 en la Tab 2 "¿Porqué Internet?

    Args:
        df (pl.DataFrame): Dataframe con la información
        colors (list): ancho del gráfico

    Returns:
        go.Fig: Suplots de Pies de la Libreria Plotly
    """

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'pie'}, {'type': 'pie'}]],
                        subplot_titles=("Ingresos 2014", "Ingresos 2024"))

    # Gráfico de Pie para Ingresos 2014
    fig.add_trace(go.Pie(labels=df["Tecnología"], values=df["Ingresos 2014"],
                         name="Ingresos 2014", marker=dict(colors=colors), scalegroup='one'), row=1, col=1)

    # Gráfico de Pie para Ingresos 2024 con tamaño proporcional
    fig.add_trace(go.Pie(labels=df["Tecnología"], values=df["Ingresos 2024"],
                         name="Ingresos 2024", marker=dict(colors=colors), scalegroup='one'), row=1, col=2)

    fig.update_layout(
        font=dict(color='#ffffff', size=16),
        paper_bgcolor='rgba(0,0,0,0)',
        height=600,
        annotations=[dict(text='2014', x=0.22, y=1.0, font_size=24, showarrow=False),
                     dict(text='2024', x=0.77, y=0.85, font_size=24, showarrow=False),
                     ])

    return fig

# ESTA FUNCION CREA LAS GRAFICAS 6 y 7 del Tab 2


def crear_graf_df(columns: list, names: list, colors: list, y_title: str, df: pl.DataFrame) -> px.line:
    """crear_graf_df: recibe de un mismo Dataframe la inf necesaria para graficar la tendencia de varias
                      columnas

    Args:
        columns (list): Lista con los nombres de las columnas a Graficar
        names (list): Lista con los nombres de Cada Linea en el Gráfico
        colors (list): Lista con los colores  usar en el Gráfico
        y_title (str): Titulo del eje y
        df (pl.DataFrame): Dataframe del cual se sacarán los datos a graficar

    Returns:
        px.line: Grafico tipo linea de la libreria plotly
    """

    fig = px.line()
    for i in range(3):
        fig.add_scatter(x=df['fecha'], y=df[columns[i]],
                        name=names[i], mode='lines', line=dict(color=colors[i]))
    fig.update_layout(
        xaxis_title='Periodo',
        yaxis_title=y_title,
        font=dict(color='#ffffff', size=16),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',  # Fondo de la grilla transparente
        xaxis=dict(showgrid=False, zeroline=True, linecolor='#ffffff'),
        yaxis=dict(showgrid=False, zeroline=True, linecolor='#ffffff'),
        height=580,
        margin=dict(l=100, r=0, t=0, b=0)
    )

    return fig


# ESTA FUNCION CREA LA TABLA DE LA DIAPOSITIVA 8 DEL CONTEXTO
def crear_tabla(df: pl.DataFrame) -> go.Figure:
    """crear_tabla: Crea la tabla donde se comparan las Variaciones de Ingresos
                    y accesos de las distintas tecnologías en el 04_eda_comparando_tecnologias.ipynb

    Args:
        df (pl.DataFrame): Dataframe con la información a mostrar en la tabla

    Returns:
        go.Fig: Tabla de la Libreria Plotly
    """
    df = df.with_columns([
        ((pl.col('Accesos 2024') / pl.col('Accesos 2014')) - 1).alias('Variación Accesos'),
        ((pl.col('Ingresos 2024') / pl.col('Ingresos 2014')) - 1).alias('Variación Ingresos')
    ])
    lista_varia_accesos = []
    lista_varia_ingresos = []
    for i in range(4):
        lista_varia_accesos.append(str(round((df[i, 5] * 100), 2)) + ' %')
        lista_varia_ingresos.append(str(round((df[i, 6] * 100), 2)) + ' %')

    header = dict(values=['Tecnología', 'Variación Accesos', 'Variación Ingresos'],
                  fill_color='lavender',
                  align='center')

    cells = dict(values=[
        ['Internet', 'Telefonía Móvil', 'Telefonía Fija', 'Televisión'],
        lista_varia_accesos,
        lista_varia_ingresos
    ],
        fill_color=[['#22D3EE', '#38C172', '#F6993F', '#FFED4A'],  # Colores personalizados para cada fila
                    ['#22D3EE', '#38C172', '#F6993F', '#FFED4A'],  # Colores de fondo para Variación Accesos
                    ['#22D3EE', '#38C172', '#F6993F', '#FFED4A']],  # Colores de fondo para Variación Ingresos
        align=['left', 'center', 'center'],
        height=30,
    )

    fig = go.Figure(data=[go.Table(header=header, cells=cells, columnwidth=[300, 300, 300],)])

    # Ajustar el layout para que se ajuste al tamaño de la tabla
    fig.update_layout(
        font=dict(color='black', size=18),
        paper_bgcolor='rgba(0,0,0,0)',
        width=800,
        height=600,
        margin=dict(l=300, r=0, t=170, b=0)
    )

    # Retorna la tabla
    return fig


# FUNCION QUE DEVUELVE LAS GRAFICAS DE LAS DIAPOSITIVAS 9 Y 10
def crea_graficas_9_10(df: pl.DataFrame, num_diapositiva: int) -> px.line:
    """Se encarga de Graficar las Diapositivas 9 y 10 de la Tab2 "¿Porqué Internet?

    Args:
        df (pl.DataFrame): Dataframe con los Datos a Graficar
        num_diapositiva (int): Numero de la Diapositiva a representar

    Returns:
        px.Line: Grafico de Lineas de Tendencias de Rangos de Velocidad o Tecnologias (según
        sea el parámetro num_diapositiva recibido) de la libreria Plotly Express
    """
    if num_diapositiva == 9:
        columns = ['ADSL', 'CABLEMODEM', 'FIBRA', 'WIRELESS']
        colors = ['#FFA15A', '#19D3F3', '#FF6692', '#B6E880']
    else:
        colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA']
        columns = ['Hasta 10 Mbps', '10.01 - 30 Mbps', '30.01 - 100 Mbps', 'Mayor a 100 Mbps']
    names = columns

    fig = px.line()
    for i in range(len(columns)):
        fig.add_scatter(x=df['Fecha'], y=df[columns[i]],
                        name=names[i], mode='lines', line=dict(color=colors[i]))
    fig.update_layout(
        xaxis_title='Periodo',
        yaxis_title='Cantidad de Accesos',
        font=dict(color='#ffffff', size=16),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',  # Fondo de la grilla transparente
        xaxis=dict(showgrid=False, zeroline=True, linecolor='#ffffff'),
        yaxis=dict(showgrid=False, zeroline=True, linecolor='#ffffff'),
        # width=800,
        height=580,
        margin=dict(l=100, r=0, t=0, b=0)
    )
    return fig


def retorna_grafico_tab2(numero_graf: int) -> html.Div:
    """retorna_grafico_tab2: Según sea el numero de grafico solicitado se apoya en las funciones
                             que se encuentran en este mismo archivo para solicitarles la grafica,
                             y encapsularla dentro de un dcc.Graph que va a ser contenido en un
                             contenedor html.Div.
                             Hablamos de los Graficos de la Pestaña o Tab 2 "¿Porqué Internet?

    Args:
        numero_graf (int): Numero de grafico solicitado

    Returns:
        html.Div: Componente con el Grafico a Devolver
    """
    if numero_graf in [1, 2, 4]:
        if numero_graf == 1:
            fig = crear_grafica(df_list=dfs_4, y_column='ingresos_miles',
                                list_names=list_4, colors=colors_4)
        elif numero_graf == 2:
            fig = crear_grafica(df_list=dfs_4, y_column='ingresos_dolar_miles',
                                list_names=list_4, colors=colors_4)
        else:
            fig = crear_grafica(df_list=dfs_3, y_column='accesos_100_hab',
                                list_names=list_3, colors=colors_3)
    elif numero_graf == 3:
        fig = fig = crear_graf_pie(df=df_pies, colors=colors_4)
    elif numero_graf in [5, 6, 7]:
        if numero_graf == 5:
            columns = ['total_accesos_post', 'total_accesos_pre', 'total_accesos']
            names = ['Accesos Post-Pagos', 'Accesos Pre-Pagos', 'Total Accesos']
            y_title = 'Accesos'
        elif numero_graf == 6:
            columns = ['llamadas_post_miles', 'llamadas_pre_miles', 'total_llamadas']
            names = ['Llamadas Post-Pagos (miles)', 'Llamadas Pre-Pagos (miles)', 'Total Llamadas (miles)']
            y_title = 'Llamadas'
        else:
            columns = ['minutos_post_miles', 'minutos_pre_miles', 'total_minutos']
            names = ['Minutos Post-Pagos (miles)', 'Minutos Pre-Pagos (miles)', 'Total Minutos (miles)']
            y_title = 'Minutos'
        colors = ['#9fbc12', ' #045426 ', '#38C172']
        fig = crear_graf_df(columns=columns, names=names, colors=colors,
                            y_title=y_title, df=telefonia_movil)
    elif numero_graf == 8:
        fig = crear_tabla(df=df_pies)
    elif numero_graf == 9:
        fig = crea_graficas_9_10(df=tecnologias_grafico_9.sort('Fecha'), num_diapositiva=9)
    elif numero_graf == 10:
        fig = crea_graficas_9_10(df=rangos_grafico_10.sort('Fecha'), num_diapositiva=10)

    config = {'displayModeBar': False}

    componente_graf_tab4 = html.Div([
        dcc.Graph(figure=fig, config=config)
    ])
    return componente_graf_tab4
