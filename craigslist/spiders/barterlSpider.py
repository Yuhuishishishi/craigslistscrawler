from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from craigslist.items import CraigslistItem

class CraigsListSpider(Spider):
	name = "craigslist"
	allowed_domains = ["craigslist.org"]
	start_urls = ["http://detroit.craigslist.org/bar",]

	def parse(self, response):
		sel = Selector(response)
		itemSelecter = sel.xpath('//a[@class="hdrlnk"]')
		items = []
		for item in itemSelecter:
			newItem = CraigslistItem()
			newItem['link'] = item.xpath('./@href').extract()
			newItem['name'] = item.xpath('./text()').extract()
			# parse the link
			print url
			yield Request(url=url, meta={'item': newItem}, callback=self.parse_item)
			items.append(newItem)

		yield items


	def parse_item(self, response):
		sel = Selector(response)
		newItem = response.meta['item']
		newItem['descp'] = sel.xpath('//section[@id="postingbody"]/text()').extract()
		
		return newItem

