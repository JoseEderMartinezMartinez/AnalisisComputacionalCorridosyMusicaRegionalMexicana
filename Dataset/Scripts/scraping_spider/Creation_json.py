# Script desarrollado origimalmente por José Eder como parte de la adaptación del proyecto:
# https://github.com/AbelGPenas/is-this-song-reggaeton

import os
import json

# Ruta de la carpeta donde están los archivos .txt
carpeta_letras = r"C:\Users\IngJo\OneDrive\Documentos\SEMESTRE 3\ARTICULO NARCO-CORRIDOS\LETRAS NARCO-CORRIDOS\Leras_corridos%regional_06-03"

# Lista para almacenar los datos
canciones = []

# Recorre todos los archivos en la carpeta
for archivo in os.listdir(carpeta_letras):
    if archivo.endswith(".txt"):
        # Extraer el título y el artista del nombre del archivo
        nombre_base = os.path.splitext(archivo)[0]  # Quita la extensión .txt
        partes = nombre_base.rsplit("_", 1)  # Divide en dos partes (Título, Artista)
        
        if len(partes) == 2:
            titulo, artista = partes
        else:
            titulo = nombre_base
            artista = "Desconocido"  # En caso de que falte el artista

        # Leer la letra de la canción
        with open(os.path.join(carpeta_letras, archivo), "r", encoding="utf-8") as f:
            letra = f.read().strip()  # Elimina espacios en blanco al inicio y final

        # Agregar a la lista
        canciones.append({
            "title": [titulo],   # Manteniendo el formato de lista
            "artist": [artista], # Manteniendo el formato de lista
            "lyrics": [letra]    # Guardando la letra en formato lista
        })

# Guardar en un archivo JSON
ruta_salida = os.path.join(carpeta_letras, "lyrics_expanded.json")
with open(ruta_salida, "w", encoding="utf-8") as json_file:
    json.dump(canciones, json_file, indent=4, ensure_ascii=False)

print(f"Archivo JSON creado en: {ruta_salida}")
