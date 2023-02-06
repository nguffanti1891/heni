import scrapy
from heni.items import HeniItem

class WebCrawler(scrapy.Spider):
    name = "webcrawler"
    start_urls = [
        "https://www.bearspace.co.uk/purchase"
    ]

    def parse(self, response):
        for product in response.xpath("//a[@data-hook='product-item-product-details-link']/@href").getall():
            yield response.follow(product, callback=self.listing)

        if 'page' in str(response.url):
            aux = response.xpath("//ul[@data-hook='product-list-pagination-seo']//a/@href").getall()
            next_page = aux[1] if len(aux) > 1 else None
        else:
            next_page = response.xpath("//ul[@data-hook='product-list-pagination-seo']//a/@href").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            
    def listing(self, response):
        url = response.url
        title = response.xpath("//h1[@data-hook='product-title']/text()").get()
        price = response.xpath("//meta[@property='product:price:amount']/@content").get()
        description = response.xpath("//pre[@data-hook='description']//p//text()").getall()
        media = ""
        try:
            media = description[0]
            for dim in description:
                if 'CM' in dim.upper():
                    width = dim.upper().split("X")[0]
                    height = dim.upper().split("X")[1].replace("CM","")

                    yield HeniItem(url=url, title=title, media=media, height_cm=height, width_cm=width, price_gbp=price)
        except:
            yield HeniItem(url=url, title=title, media=media, height_cm=0, width_cm=0, price_gbp=price)

