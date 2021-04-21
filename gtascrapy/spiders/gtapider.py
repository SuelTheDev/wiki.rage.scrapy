import scrapy
from scrapy.selector import Selector

from gtascrapy.items import GtascrapyItem


class GtapiderSpider(scrapy.Spider):
    name = 'gtapider'
    allowed_domains = ['wiki.rage.mp']
    start_urls = [
        'https://wiki.rage.mp/index.php?title=Masks',
        'https://wiki.rage.mp/index.php?title=Bags_and_Parachutes',
        'https://wiki.rage.mp/index.php?title=Male_Hair_Styles',
        'https://wiki.rage.mp/index.php?title=Male_Torsos',
        'https://wiki.rage.mp/index.php?title=Male_Legs',
        'https://wiki.rage.mp/index.php?title=Male_Shoes',
        'https://wiki.rage.mp/index.php?title=Male_Accessories',
        'https://wiki.rage.mp/index.php?title=Male_Undershirts',
        'https://wiki.rage.mp/index.php?title=Male_Body_Armors',
        'https://wiki.rage.mp/index.php?title=Male_Decals',
        'https://wiki.rage.mp/index.php?title=Male_Tops',

        'https://wiki.rage.mp/index.php?title=Female_Hair_Styles',
        'https://wiki.rage.mp/index.php?title=Female_Torsos',
        'https://wiki.rage.mp/index.php?title=Female_Legs',
        'https://wiki.rage.mp/index.php?title=Female_Shoes',
        'https://wiki.rage.mp/index.php?title=Female_Accessories',
        'https://wiki.rage.mp/index.php?title=Female_Undershirts',
        'https://wiki.rage.mp/index.php?title=Female_Body_Armors',
        'https://wiki.rage.mp/index.php?title=Female_Decals',
        'https://wiki.rage.mp/index.php?title=Female_Tops',


    ]

    def parse(self, response):
        lis = response.selector.css('li.gallerybox')
        componentId = response.xpath('//div[@class="mw-parser-output"]/p/b/text()').get()
        genero = "mf"
        if "Male" in response.request.url:
            genero = "m"
        elif "Female" in response.request.url:
            genero = "f"
        for li in lis:
            image = li.xpath('.//div/div[1]/div/a/img/@src').get()
            id = li.xpath('.//div/div[2]/p/text()').get()
            item = GtascrapyItem()
            item['image_url'] = 'https://wiki.rage.mp' + image
            item['id'] = int(id.strip())
            item['category_id'] = componentId.strip()
            item['genero'] = genero
            yield item
