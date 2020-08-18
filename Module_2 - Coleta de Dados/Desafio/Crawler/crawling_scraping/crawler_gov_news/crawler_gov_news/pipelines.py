
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json, codecs

class CrawlerGovNewsPipeline:
    
    def open_spider(self, spider):
        if spider.name == 'crawling_gov_news_website':
            self.file=codecs.open('crawled_pages.json', 'w', encoding='utf-8')
        elif spider.name == 'scraping_gov_news_website':
            self.file=codecs.open('scraped_items.json', 'w', encoding='utf-8')
            
        #self.file.write('[')
    
    def close_spider(self, spider):
        #self.file.write(']')
        self.file.close()

    def write_file(self, item, spider):
        line=json.dumps(dict(item), indent=4,sort_keys=True,separators=(',',':'), ensure_ascii=False) + ',\n'
        self.file.write(line)               
        
    def process_item(self, item, spider):
       # if spider.name == 'crawling_gov_news_website':
       #     item['text_news']=item['text_news'].replace('\n','')
            
        CrawlerGovNewsPipeline.write_file(self, item, spider)
        
        return item
