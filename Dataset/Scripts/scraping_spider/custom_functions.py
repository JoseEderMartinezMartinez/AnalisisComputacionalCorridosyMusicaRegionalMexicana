# Código adaptado y modificado a partir del proyecto original disponible en:
# https://github.com/AbelGPenas/is-this-song-reggaeton/blob/main/scraping_spider/middlewares.py
# El código original fue tomado como base y se realizaron modificaciones para ajustarlo a las necesidades de este proyecto:
# "Análisis Computacional de Temas, Evolución del Lenguaje, Sentimientos, Emociones e Intención en los Corridos y la Música Regional Mexicana"

from difflib import SequenceMatcher
import re

def remove_duplicate_songs(urls:list, titles:list):
    remix_positions = [titles.index(song) for song in titles if song.lower().find('remix') != -1]
    remix_positions.sort(reverse=True)
    for idx in iter(remix_positions):
        del urls[idx], titles[idx]
    idx = 1
    duplicate_positions = []
    while idx < len(titles):
        song1 = titles[idx-1]
        song2 = titles[idx]
        ratio = SequenceMatcher(None, a=song1, b=song2).find_longest_match(0, len(song1), 0, len(song2)).size / len(song1)
        if ratio > 0.5:
            duplicate_positions.append(idx)
        idx += 1
    for idx in iter(duplicate_positions):
        del urls[idx], titles[idx]
    return urls