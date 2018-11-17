import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from life.items import LifeItem

class LifeSpider(CrawlSpider):
	name = 'life'

	# limits the number of item scraped, it's optional, but in some cases you don't want to scrape to infinity
	#item_count = 0 
	
	# only allow information within this domain, don't let scrapy get out of it
	allowed_domain = ['https://lifeinformatica.com/']
	# for laptops
	start_urls = ['https://lifeinformatica.com/categoria-producto/family-ordenadores-y-portatiles/family-portatiles-y-accesorios/family-portatiles/']
	# for smartphones
	#start_urls = ['https://lifeinformatica.com/categoria-producto/family-tablets-y-moviles/family-smartphones-y-accesorios/family-smartphones/']

	rules = {
		# go through every page with the next button
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//nav[@class="electro-advanced-pagination"]/a'))),
		# go inside ever product on the page
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//div[@class="product-loop-header"]')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		item = LifeItem()
		
		# product information
		item['brand'] = response.xpath('//span[@itemprop="brand"]//text()').extract()
		item['name'] = response.xpath('//h1[@class="product_title entry-title"]//text()').extract()
		item['price'] = response.xpath('//span[@class="entero"]//text()').extract()
		item['decimals'] = response.xpath('//span[@class="decimales_precio"]//text()')[0].extract()
		item['currency'] = response.xpath('//span[@class="decimales_precio"]//text()')[1].extract()
		item['price_without_vat'] = response.xpath('//p[@class="sinIva"]//text()').extract()
		item['availability'] = response.xpath('//span[@class="no_stock"]//text()').extract()
		item['description'] = response.xpath('//div[@class="electro-description clearfix"]/p/text()').extract()
		#self.item_count += 1
		#if self.item_count > 5:
			#raise CloseSpider('item_exceeded')
		yield item
