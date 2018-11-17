# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LifeItem(scrapy.Item):

	# define the fields for your item here like:
	# name = scrapy.Field()

	# product information
	brand = scrapy.Field()
	name = scrapy.Field()
	price = scrapy.Field()
	decimals = scrapy.Field()
	currency = scrapy.Field()
	price_without_vat = scrapy.Field()
	availability = scrapy.Field()
	description = scrapy.Field()
