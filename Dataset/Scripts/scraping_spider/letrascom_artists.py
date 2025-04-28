import scrapy
import json

class LetrasComSpider(scrapy.Spider):
    name = "letrascom_artists"
    start_urls = [
        "https://www.letras.com/mais-acessadas/corridos/",   # URL de la sección de Corridos
        "https://www.letras.com/mais-acessadas/regional/"    # URL de la sección de Regional
    ]

    def parse(self, response):
        # Determinar el género basado en la URL
        genre = "corridos" if "corridos" in response.url else "regional"

        # Extraer los enlaces de los artistas
        artists = response.xpath('//ol[contains(@class, "top-list_art")]/li/a/@href').getall()

        # Limpiar la lista removiendo los slashes y dejando solo los nombres
        artist_list = [artist.strip("/").lower() for artist in artists]

        # Cargar datos previos si existen para evitar sobreescribirlos
        try:
            with open("artists.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        # Guardar la lista bajo la clave del género correspondiente
        data[genre] = artist_list

        # Guardar en un archivo JSON
        with open("artists.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        self.log(f"✅ Se guardaron {len(artist_list)} artistas en el género '{genre}' en artists.json")
