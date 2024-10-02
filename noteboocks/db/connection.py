from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

host = "localhost"
user = "root"
password = "root"
db_name = "db_labs_2"
motor_sql = "mysql"
connector_used = "pymysql"
port = 3306


# UTILIZANDO SQLALCHEMY
def engine_sqlalchemy() -> object | bool:
    """Conecta a Mysql Usando sqlAlchemy

    Returns:
        object: Conexion a Base de Datos
    """
    try:
        engine = create_engine(
            f"{motor_sql}+{connector_used}://{user}:{password}@{host}:{port}/{db_name}"
        )
        returned = engine
    except OperationalError as e:
        print(f"Error de la conexion {e}")
        returned = False
    finally:
        return returned
