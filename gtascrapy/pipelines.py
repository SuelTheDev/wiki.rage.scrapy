# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import urllib.request

from itemadapter import ItemAdapter


class GtascrapyPipeline:
    def process_item(self, item, spider):
        return item


class GtascrapyImagePipeline:
    def process_item(self, item, spider):
        if not os.path.exists('roupas/{}/{}'.format(item['genero'], item['category_id'])):
            os.makedirs('roupas/{}/{}'.format(item['genero'], item['category_id']))
        req = urllib.request.Request(
            item['image_url'],
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
            }
        )
        filedata = urllib.request.urlopen(req)
        datatowrite = filedata.read()
        with open('roupas/{}/{}/{}.png'.format(item['genero'], item['category_id'], item['id']), 'wb') as f:
            f.write(datatowrite)
        return item


