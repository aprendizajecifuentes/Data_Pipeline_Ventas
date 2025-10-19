# scripts/extract.py

import os
import pandas as pd
import requests
from dotenv import load_dotenv
from pathlib import Path

# Cargar archivo .env desde la carpeta config sin importar desde dónde se ejecute el script
env_path = r"D:\Portafolio_ChatGPT\config\db_config.env"
load_dotenv(dotenv_path=env_path)


# URLs y rutas configuradas
API_URL = os.getenv("API_URL")
RAW_PATH = "data/raw/"

print("URL de API cargada:", API_URL)

def extract_from_api():
    """Extrae productos desde una API pública (FakeStoreAPI)."""
    print("🔹 Extrayendo datos desde API...")
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        output_path = os.path.join(RAW_PATH, "productos_api.csv")
        df.to_csv(output_path, index=False)
        print(f"✅ Datos extraídos y guardados en {output_path}")
        return df
    else:
        print(f"❌ Error al obtener datos de la API: {response.status_code}")
        return pd.DataFrame()

def extract_from_csv(csv_file):
    """Carga datos de un archivo CSV local."""
    print(f"🔹 Cargando datos desde CSV: {csv_file}")
    try:
        df = pd.read_csv(csv_file)
        print(f"✅ {len(df)} registros cargados desde {csv_file}")
        return df
    except Exception as e:
        print(f"❌ Error al leer el CSV: {e}")
        return pd.DataFrame()

def main():
    os.makedirs(RAW_PATH, exist_ok=True)

    # Ejemplo de extracción
    api_data = extract_from_api()

    # Ejemplo de CSV local (crea uno simple para la prueba)
    csv_data = extract_from_csv("data/raw/clientes.csv")

    print("\n🔍 Vista previa de los datos extraídos:")
    print(api_data.head())
    print(csv_data.head())

if __name__ == "__main__":
    main()

