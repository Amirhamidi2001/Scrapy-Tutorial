from pathlib import Path

import scrapy


class AmirhamidiSpider(scrapy.Spider):
    name = "amirhamidi"

    def start_requests(self):
        urls = ["https://amirhamidi.pythonanywhere.com/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'amirhamdi.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
