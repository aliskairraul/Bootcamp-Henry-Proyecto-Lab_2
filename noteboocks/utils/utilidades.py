import requests
import polars as pl
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

reemplazar = [
    ['Caba', 'Capital Federal', 'CABA', 'CAPITAL FEDERAL', 'caba'
     'Ciudad Autonóma de Buenos Aires'],
    ['Tucuman'],
    ['Rio Negro'],
    ['Neuquen'],
    ['Entre Rios'],
    ['Cordoba']

]

correcion = [
    'Ciudad Autónoma de Buenos Aires',
    'Tucumán',
    'Río Negro',
    'Neuquén',
    'Entre Ríos',
    'Córdoba'
]


def obtener_coordenadas(provincias: list[str]) -> list[dict]:
    """obtener_coordenadas: Devuelve las coordenadas de las provincias de Argentina
                            que vienen en la Lista como parámetros

    Args:
        provincias (list[str]): Lista de String con los Nombres de las Provincias

    Returns:
        list[dict]: Lista de diccionarios con Provincia, Latitud, Longitud
    """

    coordenadas = []
    for provincia in provincias:
        url = f"https://apis.datos.gob.ar/georef/api/provincias?nombre={provincia}"
        response = requests.get(url)
        data = response.json()
        row = {}
        if data['cantidad'] > 0:
            row['provincia'] = provincia
            row['longitud'] = data['provincias'][0]['centroide']['lon']
            row['latitud'] = data['provincias'][0]['centroide']['lat']
            coordenadas.append(row)
    return coordenadas


def crear_tabla(df: pl.DataFrame, width: int, height: int) -> go.Fig:
    """crear_tabla: Crea la tabla donde se comparan las Variaciones de Ingresos
                    y accesos de las distintas tecnologías en el 04_eda_comparando_tecnologias.ipynb

    Args:
        df (pl.DataFrame): Dataframe con la información a mostrar en la tabla
        width (int): Ancho de la Tabla
        height (int): Alto de la Tabla

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
        align=['left', 'center', 'center'])

    fig = go.Figure(data=[go.Table(header=header, cells=cells)])

    # Ajustar el layout para que se ajuste al tamaño de la tabla
    fig.update_layout(
        width=width,
        height=height,
        margin=dict(l=10, r=10, t=10, b=10)
    )

    # Retorna la tabla
    config = {'displayModeBar': False}
    return fig(config=config)


def crear_graf_pie(df: pl.DataFrame, width: int) -> go.Fig:
    """crear_graf_pie: Crea un Subplot de Pies de Plotly. Es llamada desde el archivo
                       04_eda_comparando_tecnologias.ipynb para crear los pies que muestran la comparación
                       de ingresos en Dolares entre 2014 y 2024

    Args:
        df (pl.DataFrame): Dataframe con la información
        width (int): ancho del gráfico

    Returns:
        go.Fig: Suplots de Pies de la Libreria Plotly
    """
    proporcion = df["Ingresos 2024"].sum() / df["Ingresos 2014"].sum() * 100

    # Colores personalizados
    colors_4 = ['#22D3EE', '#38C172', '#F6993F', '#FFED4A']

    # Crear subplots
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'pie'}, {'type': 'pie'}]],
                        subplot_titles=("Ingresos 2014", "Ingresos 2024"))

    # Gráfico de Pie para Ingresos 2014
    fig.add_trace(go.Pie(labels=df["Tecnología"], values=df["Ingresos 2014"],
                         name="Ingresos 2014", marker=dict(colors=colors_4), scalegroup='one'), row=1, col=1)

    # Gráfico de Pie para Ingresos 2024 con tamaño proporcional
    fig.add_trace(go.Pie(labels=df["Tecnología"], values=df["Ingresos 2024"],
                         name="Ingresos 2024", marker=dict(colors=colors_4), scalegroup='one'), row=1, col=2)

    pie_pagina = f'Nota: Para el Año 2024 el total de Ingresos en dolares representa un {proporcion:.2f}% con respecto al 2014'
    # Actualizar el layout
    fig.update_layout(title_text="Comparación de Ingresos (en Dolares) por Tecnología",
                      width=width,  # Ajusta el ancho aquí
                      #   height=600,  # Ajusta la altura aquí
                      annotations=[dict(text='2014', x=0.18, y=0.5, font_size=20, showarrow=False),
                                   dict(text='2024', x=0.82, y=0.5, font_size=20, showarrow=False),
                                   dict(text=pie_pagina, x=0.45, y=-0.3, font_size=14,
                                        showarrow=False, xanchor='center')])

    return fig


def crear_grafica(df_list: list, y_column: str, title: str, list_names: list, colors: list, width: int) -> px.line:
    """Crear gráfica: Función para crear gráficas de tendencias

    Args:
        df_list (list): Lista de Dataframes
        y_column (str): Columna del dataframe a graficar
        title (str): Título del gráfico
        list_names (list): Lista de Nombres de los gráficos
        colors (list): Lista de Colores
        width (int): Ancho del gráfico en pixeles

    Returns:
        px.line: Grafica de linea de la Libreria plotly
    """
    fig = px.line()
    # Aca esto es como 3 ciclos for en paralelo cada variable
    for df, name, color in zip(df_list, list_names, colors):
        fig.add_scatter(x=df["fecha"], y=df[y_column], mode='lines', name=name, line=dict(color=color))
    fig.update_layout(title=title, xaxis_title='Periodo', yaxis_title=y_column, width=width)
    return fig


def crear_graf_df(
    columns: list,
    names: list,
    colors: list,
    width: int,
    y_title: str,
    df: pl.DataFrame,
    titulo: str
) -> px.line:
    """crear_graf_df: recibe de un mismo Dataframe la inf necesaria para graficar la tendencia de varias
                      columnas

    Args:
        columns (list): Lista con los nombres de las columnas a Graficar
        names (list): Lista con los nombres de Cada Linea en el Gráfico
        colors (list): Lista con los colores  usar en el Gráfico
        width (int): ancho del Gráfico de Pixeles
        y_title (str): Titulo del eje y
        df (pl.DataFrame): Dataframe del cual se sacarán los datos a graficar
        titulo (str): Titulo del gráfico

    Returns:
        px.line: Grafico tipo linea de la libreria plotly
    """

    fig = px.line()
    for i in range(3):
        fig.add_scatter(x=df['fecha'], y=df[columns[i]],
                        name=names[i], mode='lines', line=dict(color=colors[i]))
    fig.update_layout(title=titulo, xaxis_title='Periodo', yaxis_title=y_title, width=width)
    return fig


def crear_fecha_periodo(df: pl.DataFrame) -> pl.DataFrame:
    """crear_fecha_periodo: Recibe un dataframe con las columnas `anio` y `trimestre` de tipo entero y con
                            información coherente ya que NO VALIDA NADA y devuelve el mismo DataFrame con
                            dos columnas extra que representan la fecha y un periodo tipo string

    Args:
        df (pl.DataFrame): Dataframe que recibe

    Returns:
        pl.DataFrame: Dataframe que retorna
    """
    df = df['anio', 'trimestre'].unique()
    df = df.with_columns([
        (pl.col("anio").cast(pl.String) + "-0" + pl.col("trimestre").cast(pl.String)).alias("periodo"),
        (pl.date(pl.col('anio'), (pl.col('trimestre') * 3), 30)).alias('fecha')
    ])
    df = df['periodo', 'fecha']
    return df


def crear_fecha_anio_trimestre(df: pl.DataFrame) -> pl.DataFrame:
    """crear_fecha_anio_trimestre: Recibe un dataframe con las columnas `anio` y `trimestre` de tipo entero
                                   y con información coherente ya que NO VALIDA NADA y devuelve el mismo
                                   DataFrame con una columna extra que representa la fecha

    Args:
        df (pl.DataFrame): Dataframe que recibe

    Returns:
        pl.DataFrame: Dataframe que retorna
    """
    df = df['anio', 'trimestre'].unique()
    df = df.with_columns([
        (pl.date(pl.col('anio'), (pl.col('trimestre') * 3), 30)).alias('fecha')
    ])
    return df
