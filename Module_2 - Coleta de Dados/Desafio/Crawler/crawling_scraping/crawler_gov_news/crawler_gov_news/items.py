# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScraperGovNewsItem(scrapy.Item):
    title_main=scrapy.Field()
    url=scrapy.Field()
    subject=scrapy.Field()
    title_subject=scrapy.Field()
    url_subject=scrapy.Field()


class CrawlerGovNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title_page=scrapy.Field()
    url_page=scrapy.Field()
    subject_news=scrapy.Field()
    title_news=scrapy.Field()
    subtitle_news=scrapy.Field()
    text_news=scrapy.Field()
    author_news=scrapy.Field()
    category_news=scrapy.Field()
    tags_news=scrapy.Field()