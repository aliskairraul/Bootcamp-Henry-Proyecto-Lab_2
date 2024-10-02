<div style="text-align: center; border-top: 1px solid #ccc; border-bottom: 1px solid #ccc; padding: 10px 0;">
    <h1 style="color: lightblue; font-size: 2em;">Proyecto Labs 2</h1>
</div>

## Descripción

<p style="text-align: justify; text-indent: 2em;">
Este proyecto se centra en un exhaustivo análisis del sector de las telecomunicaciones en Argentina, utilizando datos extraídos del Ente Nacional de Comunicaciones (ENACOM). Se a estudiado la evolución de los ingresos y la penetración de mercado en los sectores de Telefonía Fija, Telefonía Móvil, Internet y Televisión, a lo largo de la última década.</p>

<p style="text-align: justify; text-indent: 2em;">
EL análisis se profundiza especialmente en el sector de Internet, donde se examinó el comportamiento del mercado en relación con las tecnologías que brindan el servicio, tales como ADSL, WIRELESS, Fibra Óptica y Cable Modem, y las Velocidades Medias de Descargas, tanto a nivel Nacional como de Provincias.</p>

<p style="text-align: justify; text-indent: 2em;">
Para una mejor comprensión del comportamiento del sector se empleo el uso de dos(2) KPI's a nivel de Provincias y tres(3) Métricas Nacionales, todas ellas de seguimiento trimestral.</p>

<p style="text-align: justify; text-indent: 2em;">
Los KPI empleados fueron:</p>

- **Crecimiento Trimestral de 2% en el número de Accesos por cada 100 Hogares por Provincia**:
  <p style="text-align: justify; text-indent: 2em;">
  Donde el Objetivo para el siguiente Trimestre se fijará simplemente añadiendo un 2% a los accesos por cada 100 Hogares del trimestre actual. Y cuando lleguemos en el tiempo al siguiente trimestre, la Medición del cumplimiento de dicho objetivo sería de la siguiente manera:</p>
  <br>

$$
\text{Cumplimiento KPI} = \left( \frac{\text{Acc 100 Hog Trim}}{\text{Objetivo KPI}} \right) \times 100
$$

<br>
<br>
- **Crecimiento Trimestral de 5% en la Velocidad Media de Bajada por Provincia**:
  <p style="text-align: justify; text-indent: 2em;">
  Donde el Objetivo para el siguiente Trimestre se fijará simplemente añadiendo un 5% a la velocidad del Trimestre actual. Y cuando lleguemos en el tiempo al siguiente trimestre, la Medición del cumplimiento de dicho objetivo sería de la siguiente manera:</p>
  <br>

$$
\text{Cumplimiento KPI} = \left( \frac{\text{Vel Mbps Trim}}{\text{Objetivo KPI}} \right) \times 100
$$

<br>
<br>
      <p style="text-align: justify; text-indent: 2em;">
      Las Métricas utilizadas fueron:</p>

- **Variación Trimestral del número de Accesos por cada 100 Hogares en el País**:
  <p style="text-align: justify; text-indent: 2em;">
  El cálculo de la métrica se realiza de la siguiente manera:</p>
  <br>

$$
\text{Var Accesos 100 Hog} = \left( \frac{\text{Accesos Trimestre}}{\text{Accesos Trimestre Anterior}} - 1 \right) \times 100
$$

<br>
<br>
- **Variación Trimestral de la Velocidad Media de Bajada en el País**:
    <p style="text-align: justify; text-indent: 2em;">
    El cálculo de la métrica se realiza de la siguiente manera:</p>
  <br>

$$
\text{Var Mbps} = \left( \frac{\text{Vel Mbps Trim}}{\text{Vel Mbps Trim Anterior}} - 1 \right) \times 100
$$

<br>
<br>
- **Total de Accesos en el País**:
  <p style="text-align: justify; text-indent: 2em;">
   Simplemente se monitorea el <b>Total de Accesos en el país en el Trimestre en curso</b>
  <br>

<p style="text-align: justify; text-indent: 2em;">
Para facilitar la comprensión y visualización de los datos, desarrollamos una herramienta interactiva utilizando Python y el framework Dash de la librería Plotly. Esta herramienta permite a los usuarios explorar los datos de manera intuitiva y obtener insights valiosos.</p><br>
<br>
<image src='assets/capture_tooltip.png'><br>
<br>
<image src='assets/capture_mapa_oportunidades.png'><br>
<br>

<p style="text-align: justify; text-indent: 2em;">
Previo al análisis, normalizamos los datos y creamos un modelo de datos en SQL (EDR) funcional para la empresa, que sirve como un data warehouse. Este modelo no solo organiza los datos de manera eficiente, sino que también está diseñado para soportar futuros estudios y análisis. EL EDR creado se puede observar en la siguiente Imagen<br></p>
<br>

<image src='noteboocks/assets/edr.png'>

<p style="text-align: justify; text-indent: 2em;">
Este proyecto no sdlo demuestra habilidades técnicas en análisis de datos y visualización, sino también una comprensión profunda del sector de telecomunicaciones y la capacidad de transformar datos complejos en información útil para la toma de decisiones estratégicas.</p>

## Tabla de contenido

1. [Descripción](#descripción)
1. [Enlaces](#enlaces)
1. [Instalación y Requisitos](#instalación-y-requisitos)
1. [Estructura del Proyecto](#estructura-del-proyecto)
1. [Uso y Ejecución](#uso-y-ejecución)
1. [Datos y Fuentes](#datos-y-fuentes)
1. [Metodología](#metodología)
1. [Conclusiones y Recomendaciones](#resultados-y-conclusiones)
1. [Autores](#autores)

## Enlaces

- **Enlace al repositorio**
  - https://github.com/aliskairraul/Bootcamp-Henry-Proyecto-Lab_2.git

## Instalación y Requisitos

**Requisitos:**

- Requisitos para la app

  - Python 3.10
  - dash==2.16.1
  - dash_daq==0.5.0
  - pandas==2.2.2
  - plotly==5.21.0
  - polars==1.2.1
  - pyarrow==17.0.0

- Requisitos para los Notebooks
  - Python 3.10
  - jupyter==1.1.1
  - pandas==2.2.2
  - polars==1.7.1
  - plotly==5.24.1
  - fastexcel==0.11.6
  - duckdb==1.1.0
  - pyarrow==17.0.0
  - sqlalchemy==2.0.35
  - PyMySQL==1.1.1

**Pasos de instalación:**

1. Clonar el repositorio: `git clone https://github.com/aliskairraul/Bootcamp-Henry-Proyecto-Lab_2.git`
2. Partamos del echo de que esto debe tratarse como 2 sub-proyectos por separado (un Análisis y una Aplicación realizada en Dash). Cree dos carpetas dentro de su ordenador

- Una Carpeta va todo lo referente al análisis y el modelo (Allí va a copiar sólo la Carpeta `notebooks` de este repositorio)
- En la otra Carpeta tendrá todo lo referente a la App de Dash (Allí va `TODO el Repositorio, excepto la Carpeta notebooks`)

4. Crear un entorno virtual en cada carpeta: `python3.10 -m venv nombre_del_entorno`
5. El Archivo `requirements.txt` en la raiz del proyecto son las dependencias para la App realizada en Dash y es el que debe usar para la carpeta en que tenga dicha App
6. El Archivo `requirements.txt` que se encuentra dentro de la carpeta `notebooks` es el que debe usar para instalar las dependencias del análisis
7. Activar en cada proyecto el entorno virtual:
   - Windows: `nombre_del_entorno\Scripts\activate`
   - macOS/Linux: `source nombre_del_entorno/bin/activate`
8. Instalar las dependencias: `pip install -r requirements.txt`

## Estructura del Proyecto

1. **Para la parte del Análisis**<br>

- `notebooks/`
  - Incluye los siguiente:
  - `assets/`
    - Imagenes ilustrativas.
  - `tablas/`
    - Aca se guardaran los archivos con estructura similar al EDR de la descripción del proyecto.
  - `tablas_dash/`
    - Aca se guardaran tablas especialmenete creadas para darle velocidad a la herramienta de visualización cuando interactúe con el usuario.
  - `db/`
    - Contiene los siguientes archivos:
      - `db/connection.py` Se encarga de la conección con la Base de datos Mysql
      - `db/tables.py` Tiene TODA la estructura del EDR desarrollada en el ORM SqlAlchemy de Python. Funcional para cualquier motor de base de datos SQL, contiene Todas las tablas y sus relaciones.
      - `db/create_tables.py` Script de Python que al ejecutarlo crea la base de tablas y relaciones de la Base de datos
  - `docker/`
    - contiene los siguientes archivos
      - `docker/Dockerfile` Dockerfile de la imagen Mysql
      - `docker/pasos_en_la_terminal.txt` Explicación de lo concerniente a Docker y Mysql
  - `utils/`
    -Contiene archivos con extensión `.py` que tienen funciones que dan soporte a los cuadernos Jupyter notebooks.
  - `01_normalizando_internet.ipynb`
    - Normalización de los datos contenidos en el archivo Internet.xlsx
  - `02_normalizando_otros.ipynb`
    - Normalización de los datos contenidos en los archivos
      - Telefonia_fija.xlsx
      - Telefonia_movil.xlsx
      - Television.xlsx
  - `03_creando_data_tablero.ipynb`
    - Donde se crean unas tablas customizadas para la herramineta de Visualización
  - `04_eda_comparando_tecnologias.ipynb`
    - Análisis de la evolución de los distintos sectores de las telecomunicaciones
  - `05_eda_internet.ipynb`
    - Análisis enfocado en el sector Internet de las telecomunicaciones

2. **Para la parte de la App Dash - Herramineta de Visualización**

- `data/`: Contiene los archivos `parquet` necesarios para la visualización.
- `components/`: Carpeta donde se guardan los archivos `.py ` que contienen los distintos componentes de la visualización.
- `utils/` Guarda un archivo `.py` donde se realizan unos filtros necesarios en la visualización del Mapa de Oportunidades.
- `main.py` Arhivo raiz de la App de Dash
- `requirements.txt` dependencias necesarias para la App
- `README.md`: Archivo de documentación del proyecto.

## Uso y Ejecución

1. **Para la parte del Análisis**:

- Ejecute los siguientes archivos en el Orden que se nombran a continuación:
  - `01_normalizando_internet.ipynb`
  - `02_normalizando_otros.ipynb`
  - `03_creando_data_tablero.ipynb`
  - `04_eda_comparando_tecnologias.ipynb`
  - `05_eda_internet.ipynb`

2. **Para la parte de la App de Dash, la Visualización**:

- Asegurese de que la estructura de este repositorio, a excepción de la Carpeta `notebooks`, se copió Integramente en la locación de su computador que dispuso para ello.
- Con el entorno virtual activado ejecute `python main:app` espere que se ejecute y desde el navegador `http://127.0.0.1:8050` para que vaya directamente en la visualización desde su navegador.

## Datos y Fuentes

<p style="text-align: justify; text-indent: 2em;">
Los Datasets Iniciales fueron extraídos de la  del Ente Nacional de Comunicaciones (ENACOM) de Argentina, en su gran Mayoria, sólo el archivo <b>tipos-de-cambio-historicos.csv</b> no viene de allí, este se saco de la pagina del Banco Central de Argentina. 
</p>
<br>

## Metodología

1. **Recolección de Datos**
<p style="text-align: justify; text-indent: 2em;">
Los datos utilizados en este proyecto fueron extraídos del Ente Nacional de Comunicaciones (ENACOM) de Argentina. Se recopilaron datos históricos de los últimos diez años sobre los ingresos y la penetración de mercado en los sectores de Telefonía Fija, Telefonía Móvil, Internet y Televisión.
</p>

2. **Normalización de Datos**
<p style="text-align: justify; text-indent: 2em;">
Antes de proceder con el análisis, se normalizaron los datos para asegurar su consistencia y precisión. Este proceso incluyó la limpieza de datos, la eliminación de duplicados y la corrección de valores Nulos.
</p>

3. **Creación del Modelo de Datos (EDR)**
<p style="text-align: justify; text-indent: 2em;">
Se diseñó y creó un modelo de datos en SQL (EDR) que sirve como data warehouse para la empresa. Este modelo organiza los datos de manera eficiente y está preparado para soportar futuros estudios y análisis.
</p>

4. **Análisis de Datos**
<p style="text-align: justify; text-indent: 2em;">
El análisis se centró en la evolución de los ingresos y la penetración de mercado en los sectores mencionados. Se realizó un estudio detallado del sector de Internet, examinando el comportamiento del mercado en relación con las tecnologías que brindan el servicio, tales como ADSL, WIRELESS, Fibra Óptica y Cable Modem y las distintas Velocidades Medias de Bajada que presentan las conexiones.
</p>

5. **Definición de KPI’s y Métricas**
<p style="text-align: justify; text-indent: 2em;">
Para una mejor comprensión del comportamiento del sector, se definieron dos KPI’s a nivel de provincias y tres métricas nacionales, todas ellas de seguimiento trimestral, y se encuentran a detalle en la parte de <b>Descripción</b> de este Documento
</p>

6. **Visualización de Datos**
<p style="text-align: justify; text-indent: 2em;">
Se desarrolló una herramienta interactiva de visualización utilizando Python y el framework Dash de la librería Plotly. Esta herramienta permite a los usuarios explorar los datos de manera intuitiva y obtener insights valiosos.
</p>

7. **Documentación y Presentación**
<p style="text-align: justify; text-indent: 2em;">
Finalmente, se documentaron todos los procesos y resultados del análisis. La documentación incluye la descripción del modelo de datos, los métodos de análisis utilizados, y las visualizaciones generadas. Esta documentación está diseñada para ser clara y accesible, facilitando su uso por parte de otros analistas y compañeros dentro de la Empresa.
</p>

## Conclusiones

1. **Impacto de la Inflación y Devaluación**:
<p style="text-align: justify; text-indent: 2em;">
La comparación de la evolución del mercado en dólares y pesos Argentinos muestra resultados significativamente diferentes, lo que sugiere la presencia de inflación y/o devaluación durante el período estudiado. Es crucial consultar con economistas y expertos locales antes de realizar inversiones para comprender mejor la situación económica actual.
</p>

2. **Reducción de Ingresos en el Sector de Telecomunicaciones**:
<p style="text-align: justify; text-indent: 2em;">
En la última década, los ingresos en dólares de los distintos sectores de telecomunicaciones se han reducido a la mitad. El sector de Internet es el único que ha experimentado una caída leve en ingresos, mientras que su penetración en el mercado ha seguido aumentando. Sin embargo, no se dispone de datos sobre los costos de masificación de estas tecnologías, lo que limita el análisis completo del sector.
</p>

3. **Preferencias del Mercado**:
<p style="text-align: justify; text-indent: 2em;">
Los datos indican una clara preferencia de los consumidores argentinos por servicios de Internet que ofrecen mayores velocidades. Esto se refleja en la disminución drástica de la participación de mercado de la tecnología ADSL y el aumento en la velocidad media de bajada de Internet en los últimos tres años. Las tecnologías dominantes en el mercado actual son CableModem y Fibra Óptica, aunque ambas requieren infraestructura de cableado, lo que puede no ser rentable en áreas de baja densidad poblacional.
</p>

## Recomendaciones

1. **Consulta con Expertos Económicos**:
<p style="text-align: justify; text-indent: 2em;">
Antes de realizar inversiones en el sector de telecomunicaciones en Argentina, es recomendable consultar con economistas y expertos locales para obtener una comprensión detallada de la situación económica y los posibles riesgos asociados.
</p>

2. **Análisis de Costo-Beneficio**:
<p style="text-align: justify; text-indent: 2em;">
Realizar un análisis de costo-beneficio detallado del sector de Internet es esencial antes de incursionar en él. Esto ayudará a identificar las oportunidades y desafíos específicos del mercado y a tomar decisiones informadas.
</p>

3. **Exploración de Tecnologías Inalámbricas**:
<p style="text-align: justify; text-indent: 2em;">
Dado que las tecnologías CableModem y Fibra Óptica tienen limitaciones en áreas de baja densidad poblacional, se recomienda estudiar la viabilidad de tecnologías inalámbricas de alta velocidad, como la tecnología satelital, para penetrar en estos mercados. Esto podría representar una gran oportunidad para expandir la cobertura de Internet en localidades con menor número de habitantes.
</p>

## Autores:

Este proyecto fue realizado por: Aliskair Rodríguez.<br>
[linkedin.com/in/aliskair-rodriguez-782b3641](https://www.linkedin.com/in/aliskair-rodriguez-782b3641/)
