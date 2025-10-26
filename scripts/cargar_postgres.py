import pandas as pd
from sqlalchemy import create_engine

# Datos de conexión //deben ir en archivo .venv para no ser publicados.

usuario = 'postgres'
password = 'tu_contraseña'
host = 'localhost'
puerto = '5432'
base_datos = 'portafolio_datos'

# Crear conexión
engine = create_engine('postgresql+psycopg2://postgres:1802701@localhost:5432/portafolio_datos')


# Leer CSV
clientes = pd.read_csv(r'D:\Portafolio_ChatGPT\data\processed\clientes_limpios.csv')
productos = pd.read_csv(r'D:\Portafolio_ChatGPT\data\processed\productos_limpios.csv')

ventas_path = r"D:\Portafolio_ChatGPT\data\processed\ventas.csv"
ventas = pd.read_csv(ventas_path)

# Cargar en PostgreSQL
clientes.to_sql('clientes', engine, if_exists='replace', index=False)
productos.to_sql('productos', engine, if_exists='replace', index=False)
ventas.to_sql("ventas", engine, if_exists="replace", index=False)

print("Tabla 'ventas' cargada correctamente en PostgreSQL.")
print("Datos cargados correctamente en PostgreSQL")
