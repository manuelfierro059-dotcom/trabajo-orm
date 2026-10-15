import os
from urllib.parse import quote_plus


class Config:

    USER = os.getenv('DB_USER', 'postgres')
    PASSWORD = os.getenv('DB_PASSWORD', '345705374')
    HOST = os.getenv('DB_HOST', 'localhost')
    PORT = os.getenv('DB_PORT', '5432')
    DATABASE = os.getenv('DB_NAME', 'db_productos')

    _encoded_pwd = quote_plus(PASSWORD) if PASSWORD else ''
    _auth = f"{USER}:{_encoded_pwd}@" if _encoded_pwd else f"{USER}@"

    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{_auth}{HOST}:{PORT}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

