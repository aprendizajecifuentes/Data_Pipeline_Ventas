import pandas as pd
import os

RAW_DIR = r"D:\Portafolio_ChatGPT\data\raw"
PROCESSED_DIR = r"D:\Portafolio_ChatGPT\data\processed"

# Crear carpeta processed si no existe
os.makedirs(PROCESSED_DIR, exist_ok=True)

def limpiar_productos(df):
    """Limpieza de datos de productos"""
    df = df.copy()
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['title', 'price'], inplace=True)
    df['title'] = df['title'].str.strip().str.lower()
    df['price'] = df['price'].astype(float)
    return df

def limpiar_clientes(df):
    """Limpieza de datos de clientes"""
    df = df.copy()
    df.drop_duplicates(inplace=True)
    df['nombre'] = df['nombre'].str.title()
    df['pais'] = df['pais'].str.title()
    df['edad'] = df['edad'].astype(int)
    return df

def main():
    print("Cargando datos crudos...")
    
    productos = pd.read_csv(os.path.join(RAW_DIR, "productos_api.csv"))
    clientes = pd.read_csv(os.path.join(RAW_DIR, "clientes.csv"))

    print("Limpieza de productos...")
    productos_limpios = limpiar_productos(productos)

    print("Limpieza de clientes...")
    clientes_limpios = limpiar_clientes(clientes)

    print("Guardando datos procesados...")
    productos_limpios.to_csv(os.path.join(PROCESSED_DIR, "productos_limpios.csv"), index=False)
    clientes_limpios.to_csv(os.path.join(PROCESSED_DIR, "clientes_limpios.csv"), index=False)

    print("Transformación completada correctamente.")

if __name__ == "__main__":
    main()
