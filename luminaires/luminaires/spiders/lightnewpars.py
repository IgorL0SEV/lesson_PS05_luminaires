import scrapy


class LightnewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["http://divan.ru/"]
    start_urls = ["http://divan.ru/category/svet"]

    def parse(self, response):
        pass
