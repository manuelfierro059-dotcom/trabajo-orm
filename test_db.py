import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app.common.config import Config

def init_postgres():
    user = Config.USER
    password = Config.PASSWORD
    host = Config.HOST
    port = Config.PORT
    db_name = Config.DATABASE

    print(f"Conectando a PostgreSQL ({host}:{port}) con usuario '{user}'...")
    try:
        # Conexión al catálogo inicial 'postgres' para verificar/crear la base de datos
        conn = psycopg2.connect(
            dbname='postgres',
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
        if not cursor.fetchone():
            print(f"Creando base de datos '{db_name}' en PostgreSQL...")
            cursor.execute(f'CREATE DATABASE "{db_name}"')
            print(f"¡Base de datos '{db_name}' creada exitosamente!")
        else:
            print(f"La base de datos '{db_name}' ya existe en PostgreSQL.")
            
        cursor.close()
        conn.close()

        # Probar conexión directa a la base de datos destino
        conn_target = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn_target.close()
        print("¡Conexión verificada con éxito!")
        return True

    except Exception as e:
        print(f"Error de conexión a PostgreSQL: {e}")
        return False

if __name__ == "__main__":
    success = init_postgres()
    sys.exit(0 if success else 1)
