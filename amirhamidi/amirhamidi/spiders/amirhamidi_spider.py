# Data extraction and stored in HTML format
# Running the project with command: scrapy crawl amirhamidi

# from pathlib import Path

# import scrapy


# class AmirhamidiSpider(scrapy.Spider):
#     name = "amirhamidi"

#     def start_requests(self):
#         urls = ["https://amirhamidi.pythonanywhere.com/"]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f'amirhamdi.html'
#         Path(filename).write_bytes(response.body)
#         self.log(f'Saved file {filename}')




# Data extraction and stored in json format
# Running the project with command: scrapy crawl amirhamidi -O amirhamidi.json

# import scrapy


# class AmirhamidiSpider(scrapy.Spider):
#     name = "amirhamidi"
#     allowed_domains = ["amirhamidi.pythonanywhere.com"]
#     start_urls = ["http://amirhamidi.pythonanywhere.com/"]

#     def parse(self, response):

#         for href in response.xpath('//a/@href').getall():
#             yield {"title": href}







# Data extraction and stored in jl format
# Running the project with command: scrapy crawl amirhamidi -O amirhamidi.jl

import scrapy


class AmirhamidiSpider(scrapy.Spider):
    name = "amirhamidi"
    allowed_domains = ["amirhamidi.pythonanywhere.com"]

    def start_requests(self):
        yield scrapy.Request("http://amirhamidi.pythonanywhere.com/", self.parse)

    def parse(self, response):

        for href in response.xpath('//a/@href').getall():
            yield {"title": href}
