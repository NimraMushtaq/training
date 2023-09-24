from abc import ABC, abstractmethod
import scrapy
from myscraper.items import ProductItems


class BaseSpider(ABC, scrapy.Spider):
    allowed_domains = ["www.paklap.pk"]
    def parse(self, response):
        products = response.css('li.product-item')

        for product_item in products:
            product_url = product_item.css('a.product-item-link::attr(href)').get()

            if product_url is not None:
                yield response.follow(product_url, callback=self.parse_product_page)

        next_page = response.css('a.action.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    @abstractmethod
    def parse_product_page(self, response):
        pass


class LaptopSpiderSpider(BaseSpider):
    name = "laptop_spider"
    custom_settings = {
        'ITEM_PIPELINES': {
            'myscraper.pipelines.LaptopPipeline': 300,
        }
    }
    start_urls = ['https://www.paklap.pk/apple-products/apple-macbooks.html',
                  'https://www.paklap.pk/laptops-prices.html']

    def parse_product_page(self, response):
        product_item = ProductItems()

        product_item['name'] = response.css('h1.page-title span.base::text').get()
        product_item['color'] = response.css('th:contains("Color") + td.col.data::text').get()
        product_item['weight'] = response.css('th:contains("Weight") + td.col.data::text').get()
        product_item['screen_resolution'] = response.css('th:contains("Screen resolution") + td.col.data::text').get()
        product_item['screen_size'] = response.css('th:contains("Screen size") + td.col.data::text').get()
        product_item['ssd'] = response.css('th:contains("SSD") + td.col.data::text').get()
        product_item['installed_ram'] = response.css('th:contains("Installed RAM") + td.col.data::text').get()
        product_item['generation'] = response.css('th:contains("Generation") + td.col.data::text').get()
        product_item['brand'] = response.css('th:contains("Brand") + td.col.data::text').get()
        product_item['price'] = response.css('span.price-wrapper span.price::text').get()

        yield product_item
