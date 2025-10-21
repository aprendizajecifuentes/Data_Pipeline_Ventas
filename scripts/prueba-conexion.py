import os

ruta = r"D:\Portafolio_ChatGPT\config\db_config.env"

print("📁 Comprobando si existe el archivo .env...\n")

print("Ruta esperada:", ruta)
print("Existe?:", os.path.exists(ruta))

if os.path.exists(ruta):
    print("\n✅ Python puede ver el archivo correctamente.")
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()
    print("\nContenido del archivo .env:\n")
    print(contenido)
else:
    print("\n❌ Python NO puede encontrar el archivo.")
    print("\nContenido del directorio actual:")
    print(os.listdir("D:\\Portafolio_ChatGPT"))
