import polars as pl


def retorna_dfs_graficos_tab4(
        df_accesos_localidades: pl.DataFrame,
        df_rangos: pl.DataFrame,
        hab_minimo: int,
        hab_maximo: int) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame, int, int]:
    """retorna_dfs_graficos_tab4: Es llamada desde la Callback que actualiza el TAB 4 o
                                  'Mapa de Oportunidades` en la visualización. Se encarga de preparar la
                                  data para los distintos componentes de esa pestaña de la visualización

    Args:
        df_accesos_localidades (pl.DataFrame): Dataframe con la Data de todas las localidades
        df_rangos (pl.DataFrame): Dataframe con la data de los Rangos de Velocidad asociados a las localidades
        hab_minimo (int): Rango inferior de habitantes selecionado por el usuario
        hab_maximo (int): Rango superior de Habitantes selecionado por el usuario

    Returns:
        tuple[pl.DataFrame,pl.DataFrame, pl.DataFrame, int, int]:
                df_mapa: Dataframe con información de localidades seleccionadas con sus latitudes y longitudes
                         e informacion para el tooltip
                df_pie_rangos: Dataframe que va dirigido a alimentar el Grafico de Pie de Rango de Velocidades
                df_tecnologias: Dataframe que va dirigido a alimentar el Grafico de Pies de las Tecnologias
                total_accesos: Dato que se muestra en la Seccion Izquierda de la pestaña, donde se muestra texto
                total_localidades:Dato que se muestra en la Seccion Izquierda de la pestaña, donde se muestra texto



    """
    '''Obteniendo la Data que va para el Mapa, df_mapa'''
    mask = (df_accesos_localidades['Población'] >= hab_minimo) &\
        (df_accesos_localidades['Población'] <= hab_maximo)

    # Esta lista de Localidades (en el rango de poblacion) la utilizaré para filtrar en el
    # dataframe de rangos de velocidades
    lista_ids_localidades = df_accesos_localidades.filter(mask)['id_localidad'].to_list()
    total_localidades = len(lista_ids_localidades)

    columns = ['Provincia', 'Partido', 'Localidad', 'Población', 'Accesos 100 Hab', 'Longitud', 'Latitud']
    df_mapa = df_accesos_localidades.filter(mask)[columns]

    '''Obteniendo la Data para el grafico que clasifica por tipo de Tecnologia'''
    df_tecnologias = pl.DataFrame()
    adsl = df_accesos_localidades.filter(mask)['ADSL'].sum()
    cable_modem = df_accesos_localidades.filter(mask)['CABLEMODEM'].sum()
    fibra = df_accesos_localidades.filter(mask)['FIBRA'].sum()
    wireless = df_accesos_localidades.filter(mask)['WIRELESS'].sum()
    satelital = df_accesos_localidades.filter(mask)['SATELITAL'].sum()
    winmax = df_accesos_localidades.filter(mask)['WINMAX'].sum()
    tecnologias = [adsl, cable_modem, fibra, wireless, satelital, winmax]
    columns = ['ADSL', 'CABLEMODEM', 'FIBRA', 'WIRELESS', 'SATELITAL', 'WINMAX']
    for i in range(6):
        df_tecnologias = df_tecnologias.with_columns(pl.lit(tecnologias[i]).alias(columns[i]))

    '''Obteniendo la Data que va para el Pie con Rangos de Velocidades, df_pie_rangos'''
    df_pie_rangos = pl.DataFrame()
    rangos = ['Hasta 10 Mbps', '10.01 - 30 Mbps', '30.01 - 100 Mbps', 'Mayor a 100 Mbps']
    velocidades = [(0, 10), (10.01, 30), (30.01, 100), (100.01, 1000000)]

    total_accesos = 0
    for i in range(4):
        menor = velocidades[i][0]
        mayor = velocidades[i][1]
        mask = (df_rangos['id_localidad'].is_in(lista_ids_localidades)) &\
               (df_rangos['velocidad_mbps'].is_between(menor, mayor))
        accesos = df_rangos.filter(mask)['accesos'].sum()
        total_accesos += accesos
        df_pie_rangos = df_pie_rangos.with_columns(pl.lit(accesos).alias(rangos[i]))

    return (df_mapa, df_pie_rangos, df_tecnologias, total_accesos, total_localidades)
