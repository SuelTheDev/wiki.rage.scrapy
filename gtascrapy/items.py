# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GtascrapyItem(scrapy.Item):
    image_url = scrapy.Field()
    id = scrapy.Field()
    category_id = scrapy.Field()
    genero = scrapy.Field()
