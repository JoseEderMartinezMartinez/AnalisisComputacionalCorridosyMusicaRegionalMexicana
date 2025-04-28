# Script desarrollado origimalmente por José Eder como parte de la adaptación del proyecto:
# https://github.com/AbelGPenas/is-this-song-reggaeton

import pandas as pd
from langdetect import detect

# Cargar el archivo CSV
archivo = r"C:\Users\Joseder\Documents\Cenidet\SEMESTRE 3\ARTICULO NARCO-CORRIDOS\Documento\resultados\letras_regional.csv"  # Reemplaza con la ruta de tu archivo
df = pd.read_csv(archivo)

# Definir una función para detectar el idioma
def detectar_idioma(texto):
    try:
        return detect(texto)
    except:
        return "desconocido"

# Aplicar la función a la columna que contiene las letras de las canciones
df["idioma"] = df["lyrics"].astype(str).apply(detectar_idioma)  # Asegúrate de que la columna se llama "lyrics"

# Filtrar canciones en español
df_espanol = df[df["idioma"] == "es"]

# Filtrar canciones que NO están en español (eliminadas)
df_no_espanol = df[df["idioma"] != "es"]

# Guardar las canciones en español en un nuevo archivo
df_espanol.drop(columns=["idioma"], inplace=True)  # Eliminar la columna de idioma antes de guardar
df_espanol.to_csv("canciones_filtradas.csv", index=False)

# Guardar las canciones eliminadas con el idioma detectado
df_no_espanol.to_csv("canciones_eliminadas.csv", index=False)

print("Archivo limpio guardado como 'canciones_filtradas.csv'")
print("Canciones eliminadas guardadas en 'canciones_eliminadas.csv'")
