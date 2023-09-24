import scrapy


class ProductItems(scrapy.Item):
    name = scrapy.Field()
    color = scrapy.Field()
    weight = scrapy.Field()
    screen_resolution = scrapy.Field()
    screen_size = scrapy.Field()
    ssd = scrapy.Field()
    installed_ram = scrapy.Field()
    generation = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
