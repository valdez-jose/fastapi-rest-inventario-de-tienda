
import urllib.parse
from sqlalchemy import create_engine
# AQUÍ IMPORTAMOS LAS HERRAMIENTAS QUE TE MARCABAN ERROR:
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 1. Tus datos de conexión (Asegúrate de que tu contraseña sea la correcta)
DB_USER = "postgres"  
DB_PASSWORD = "mi-post123"  
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "inventario_tienda;"

# Codificamos la contraseña por si tiene caracteres como el '@'
password_encoded = urllib.parse.quote_plus(DB_PASSWORD)

# 2. Creamos la URL y el Motor de conexión
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{password_encoded}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. Creamos la fábrica de sesiones (Ahora sí sabe qué es sessionmaker)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Creamos la Base (Ahora sí sabe qué es DeclarativeBase)
class Base(DeclarativeBase):
    pass  # <-- Asegúrate de que tenga esta sangría (un tabulador o 4 espacios)