from tables import Model
from connection import engine_sqlalchemy

# Tablas que van a ser Creadas en el motor SQL
from tables import (
    Localidades,
    Partidos,
    Provincias,
    InternetProvincia,
    AccesosXTecnologia,
    VelocidadSinRangos,
    InternetPais,
    TelefoniaMovil,
    TelefoniaFija,
    Television
)

# Necesito crear un Engine
engine = engine_sqlalchemy()

# Creacion de Todas las Tablas del Proyecto
Model.metadata.drop_all(engine)
Model.metadata.create_all(engine)
