# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SchoolbagItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    picture = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    hot_word = scrapy.Field()
    comment = scrapy.Field()
    publisher = scrapy.Field()
