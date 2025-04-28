# Código adaptado y modificado a partir del proyecto original disponible en:
# https://github.com/AbelGPenas/is-this-song-reggaeton/blob/main/scraping_spider/middlewares.py
# El código original fue tomado como base y se realizaron modificaciones para ajustarlo a las necesidades de este proyecto:
# "Análisis Computacional de Temas, Evolución del Lenguaje, Sentimientos, Emociones e Intención en los Corridos y la Música Regional Mexicana"

import pandas as pd

def analizar_dataset(archivo):
    # Cargar el archivo CSV
    df = pd.read_csv(archivo)
    
    # Obtener el número total de canciones
    num_canciones = df.shape[0]
    
    # Obtener el número de artistas únicos
    num_artistas = df['artist'].nunique()
    
    # Imprimir resultados
    print(f"Número total de canciones: {num_canciones}")
    print(f"Número de artistas únicos: {num_artistas}")

# Especificar la ruta del archivo
dataset_path = r'C:\Users\Joseder\Downloads\is-this-song-reggaeton-main\letras_corridos_limpio.csv'

# Ejecutar la función
analizar_dataset(dataset_path)
