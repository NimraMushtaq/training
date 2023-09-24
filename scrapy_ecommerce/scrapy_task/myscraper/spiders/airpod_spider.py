import scrapy
from myscraper.items import ProductItems
from .laptop_spider import BaseSpider


class AirpodSpiderSpider(BaseSpider):
    name = "airpod_spider"
    custom_settings = {
        'ITEM_PIPELINES': {
            'myscraper.pipelines.AirpodPipeline': 400,
        }
    }
    start_urls = ['https://www.paklap.pk/catalogsearch/result/?cat=0&q=airpods']

    def parse_product_page(self, response):
        product_item = ProductItems()

        product_item['name'] = response.css('h1.page-title span.base::text').get()
        product_item['color'] = response.css('th:contains("Color") + td.col.data::text').get()
        product_item['brand'] = response.css('th:contains("Brand") + td.col.data::text').get()
        product_item['price'] = response.css('span.price-wrapper span.price::text').get()

        yield product_item
