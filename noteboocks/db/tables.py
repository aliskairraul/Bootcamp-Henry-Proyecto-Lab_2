from typing import List
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Numeric, ForeignKey, SmallInteger, BigInteger, Boolean


Model = declarative_base()


class Localidades(Model):
    __tablename__ = 'localidades'
    id_localidad: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    id_indec: Mapped[int] = mapped_column(Integer)
    id_partido: Mapped[int] = mapped_column(SmallInteger, ForeignKey("partidos.id_partido"))
    localidad: Mapped[str] = mapped_column(String(100))
    poblacion: Mapped[int] = mapped_column(Integer)
    longitud: Mapped[float] = mapped_column(Numeric(13, 10))
    latitud: Mapped[float] = mapped_column(Numeric(13, 10))
    '''RELATIONS:'''
    partido: Mapped['Partidos'] = relationship(back_populates='localidades')
    rangos_localidades: Mapped[List['RangosLocalidades']] = relationship(back_populates='localidad')
    acceso_localidad: Mapped['AccesosLocalidades'] = relationship(back_populates='localidad')


class Partidos(Model):
    __tablename__ = 'partidos'
    id_partido: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=False)
    id_provincia: Mapped[int] = mapped_column(SmallInteger, ForeignKey('provincias.id_provincia'))
    partido: Mapped[str] = mapped_column(String(80))
    '''RELATIONS:'''
    localidades: Mapped[List[Localidades]] = relationship(back_populates='partido')
    provincia: Mapped['Provincias'] = relationship(back_populates='partidos')


class Provincias(Model):
    __tablename__ = 'provincias'
    id_provincia: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=False)
    provincia: Mapped[str] = mapped_column(String(40))
    longitud: Mapped[float] = mapped_column(Numeric(13, 10))
    latitud: Mapped[float] = mapped_column(Numeric(13, 10))
    '''RELATIONS:'''
    partidos: Mapped[List['Partidos']] = relationship(back_populates='provincia')
    internet_provincias: Mapped[List['InternetProvincia']] = relationship(back_populates='provincia')
    accesos_tecnologia: Mapped[List['AccesosXTecnologia']] = relationship(back_populates='provincia')
    velocidades_sin_rangos: Mapped[List['VelocidadSinRangos']] = relationship(back_populates='provincia')


class RangosLocalidades(Model):
    __tablename__ = 'rangos_localidades'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_localidad: Mapped[int] = mapped_column(Integer, ForeignKey('localidades.id_localidad'))
    id_indec: Mapped[int] = mapped_column(Integer)
    accesos: Mapped[int] = mapped_column(Integer)
    velocidad_mbps: Mapped[float] = mapped_column(Numeric(8, 2))
    '''RELATIONS:'''
    localidad: Mapped['Localidades'] = relationship(back_populates='rangos_localidades')


class AccesosLocalidades(Model):
    __tablename__ = 'accesos_localidades'
    id_localidad: Mapped[int] = mapped_column(
        Integer, ForeignKey('localidades.id_localidad'), primary_key=True, autoincrement=False
    )
    id_indec: Mapped[int] = mapped_column(Integer)
    _3g: Mapped[bool] = mapped_column(Boolean)
    _4g: Mapped[bool] = mapped_column(Boolean)
    adsl: Mapped[int] = mapped_column(Integer)
    cablemodem: Mapped[int] = mapped_column(Integer)
    dial_up: Mapped[int] = mapped_column(Integer)
    fibra: Mapped[int] = mapped_column(Integer)
    satelital: Mapped[int] = mapped_column(Integer)
    winmax: Mapped[int] = mapped_column(Integer)
    wireless: Mapped[int] = mapped_column(Integer)
    otros: Mapped[int] = mapped_column(Integer)
    total: Mapped[int] = mapped_column(BigInteger)
    '''RELATIONS:'''
    localidad: Mapped['Localidades'] = relationship(back_populates='acceso_localidad')


class InternetProvincia(Model):
    __tablename__ = 'internet_provincia'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    anio: Mapped[int] = mapped_column(SmallInteger)
    trimestre: Mapped[int] = mapped_column(SmallInteger)
    accesos_100_hog: Mapped[float] = mapped_column(Numeric(5, 2))
    accesos_100_hab: Mapped[float] = mapped_column(Numeric(5, 2))
    accesos_banda_ancha: Mapped[int] = mapped_column(Integer)
    accesos_dial_up: Mapped[int] = mapped_column(Integer)
    mbps_media_bajada: Mapped[float] = mapped_column(Numeric(8, 2))
    id_provincia: Mapped[int] = mapped_column(SmallInteger, ForeignKey('provincias.id_provincia'))
    '''RELATIONS:'''
    provincia: Mapped['Provincias'] = relationship(back_populates='internet_provincias')


class AccesosXTecnologia(Model):
    __tablename__ = 'accesos_x_tecnologia'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    anio: Mapped[int] = mapped_column(SmallInteger)
    trimestre: Mapped[int] = mapped_column(SmallInteger)
    adsl: Mapped[int] = mapped_column(Integer)
    cablemoden: Mapped[int] = mapped_column(Integer)
    fibra: Mapped[int] = mapped_column(Integer)
    wireless: Mapped[int] = mapped_column(Integer)
    otros: Mapped[int] = mapped_column(Integer)
    total: Mapped[int] = mapped_column(BigInteger)
    id_provincia: Mapped[int] = mapped_column(SmallInteger, ForeignKey('provincias.id_provincia'))
    '''RELATIONS:'''
    provincia: Mapped['Provincias'] = relationship(back_populates='accesos_tecnologia')


class VelocidadSinRangos(Model):
    __tablename__ = 'velocidad_sin_rangos'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    anio: Mapped[int] = mapped_column(SmallInteger)
    trimestre: Mapped[int] = mapped_column(SmallInteger)
    velocidad_mbps: Mapped[float] = mapped_column(Numeric(8, 2))
    accesos: Mapped[int] = mapped_column(Integer)
    id_provincia: Mapped[int] = mapped_column(SmallInteger, ForeignKey('provincias.id_provincia'))
    '''RELATIONS:'''
    provincia: Mapped['Provincias'] = relationship(back_populates='velocidades_sin_rangos')


class InternetPais(Model):
    __tablename__ = 'internet_pais'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    anio: Mapped[int] = mapped_column(SmallInteger)
    trimestre: Mapped[int] = mapped_column(SmallInteger)
    mbps_media_bajada: Mapped[float] = mapped_column(Numeric(8, 2))
    accesos_100_hog: Mapped[float] = mapped_column(Numeric(5, 2))
    accesos_100_hab: Mapped[float] = mapped_column(Numeric(5, 2))
    ingresos_miles: Mapped[float] = mapped_column(Numeric(15, 2))


class TelefoniaMovil(Model):
    __tablename__ = 'telefonia_movil'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    anio: Mapped[int] = mapped_column(SmallInteger)
    trimestre: Mapped[int] = mapped_column(SmallInteger)
    llamadas_post_miles: Mapped[int] = mapped_column(BigInteger)
    llamadas_pre_miles: Mapped[int] = mapped_column(BigInteger)
    sms_salientes: Mapped[int] = mapped_column(BigInteger)
    minutos_post_miles: Mapped[int] = mapped_column(BigInteger)
    minutos_pre_miles: Mapped[int] = mapped_column(BigInteger)
    accesos_100_hab: Mapped[float] = mapped_column(Numeric(5, 2))
    total_accesos_post: Mapped[int] = mapped_column(Integer)
    total_accesos_pre: Mapped[int] = mapped_column(Integer)
    ingresos_miles: Mapped[float] = mapped_column(Numeric(15, 2))


class TelefoniaFija(Model):
    __tablename__ = 'telefonia_fija'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    anio: Mapped[int] = mapped_column(SmallInteger)
    trimestre: Mapped[int] = mapped_column(SmallInteger)
    accesos_hogares: Mapped[int] = mapped_column(Integer)
    accesos_comercial: Mapped[int] = mapped_column(Integer)
    accesos_gobierno: Mapped[int] = mapped_column(Integer)
    accesos_otros: Mapped[int] = mapped_column(Integer)
    accesos_100_hog: Mapped[float] = mapped_column(Numeric(5, 2))
    accesos_100_hab: Mapped[float] = mapped_column(Numeric(5, 2))
    ingresos_miles: Mapped[float] = mapped_column(Numeric(15, 2))


class Television(Model):
    __tablename__ = 'television'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    anio: Mapped[int] = mapped_column(SmallInteger)
    trimestre: Mapped[int] = mapped_column(SmallInteger)
    accesos_sate_100_hab: Mapped[float] = mapped_column(Numeric(5, 2))
    accesos_susc_100_hab: Mapped[float] = mapped_column(Numeric(5, 2))
    accesos_sate_100_hog: Mapped[float] = mapped_column(Numeric(5, 2))
    accesos_susc_100_hog: Mapped[float] = mapped_column(Numeric(5, 2))
    accesos_tot_suscripcion: Mapped[int] = mapped_column(Integer)
    accesos_tot_satelital: Mapped[int] = mapped_column(Integer)
    ingresos_suscripcion_miles: Mapped[float] = mapped_column(Numeric(15, 2))
    ingresos_satelital_miles: Mapped[float] = mapped_column(Numeric(15, 2))
