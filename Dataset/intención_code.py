##Codigo realizado por Tlaloc Humberto Vergara Morlaes
##Código para clasificar la intención de las canciones de corridos y musica reginal en general utilizando bart-large-mnli
##Se utiliza el mismo modelo sin modificaciones y solo especificando las etiquetas: "glorificar el narcotráfico", "describir el narcotráfico", "desprestigiar el narcotráfico" (sujetas a cambios/mejoras/añadiciones)
import os
import pandas as pd
from transformers import pipeline

# Configuración del modelo
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", framework="pt")

# Ruta de los archivos CSV
csv_corridos = r"...\letras_corridos_limpio.csv"
csv_regional = r"...\Letras_csv\letras_regional_limpio.csv"
entrePath = r"...\entrenamiento"

# Etiquetas de intención
candidate_labels = ["glorificar el narcotráfico", "describir el narcotráfico", "desprestigiar el narcotráfico"]

# Función para analizar un CSV
def analizar_csv(csv_path, categoria):
    df = pd.read_csv(csv_path)
    results = []
    conteo_etiquetas = {label: 0 for label in candidate_labels}
    i=0
    for index, row in df.iterrows():
        print("#",i)
        title = row["title"]
        artist = row["artist"]
        lyrics = row["lyrics"]
        
        try:
            # Analizar la letra completa
            result = classifier(lyrics.strip(), candidate_labels)
            
            # Obtener la etiqueta con el puntaje más alto
            final_label = result["labels"][0]
            final_score = result["scores"][0] * 100  # Convertir a porcentaje
            conteo_etiquetas[final_label] += 1
            
            # Guardar en la lista de resultados
            results.append([categoria, title, artist, final_label, round(final_score, 2)])
        
        except Exception as e:
            print(f"Error procesando {title} de {artist}: {e}")
        i+=1
    
    return results, conteo_etiquetas

# Analizar ambos CSVs
resultados_corridos, conteo_corridos = analizar_csv(csv_corridos, "Corridos")
resultados_regional, conteo_regional = analizar_csv(csv_regional, "Regional")

# Combinar resultados
total_results = resultados_corridos + resultados_regional

df_results = pd.DataFrame(total_results, columns=["Categoría", "Título", "Artista", "Etiqueta Identificada", "Confianza (%)"])

# Crear un DataFrame para la comparación de etiquetas
conteo_comparacion = pd.DataFrame({
    "Etiqueta": candidate_labels,
    "Corridos": [conteo_corridos[label] for label in candidate_labels],
    "Regional": [conteo_regional[label] for label in candidate_labels]
})

# Guardar en un archivo Excel con dos hojas
df_output_path = os.path.join(os.path.dirname(csv_corridos), "analisis_canciones.xlsx")
with pd.ExcelWriter(df_output_path) as writer:
    conteo_comparacion.to_excel(writer, sheet_name="Comparación de etiquetas", index=False)
    df_results.to_excel(writer, sheet_name="Análisis de canciones", index=False)

print(f"Análisis completado. Resultados guardados en {df_output_path}")
