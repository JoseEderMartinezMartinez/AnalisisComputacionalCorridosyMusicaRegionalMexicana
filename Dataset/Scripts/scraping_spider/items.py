# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from w3lib.html import remove_tags, strip_html5_whitespace
import scrapy
from itemloaders.processors import MapCompose, Join
import re


class MamasitaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace)
    )
    artist = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace)
    )
    lyrics = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=Join(' , ')
    )
