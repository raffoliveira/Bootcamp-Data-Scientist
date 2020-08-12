#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 19:01:21 2020

@author: rafael
"""
#para rodar e salvar no formato json:
#scrapy runspider script_name.py -t json -o file_name.json

#para rodar um arquivo normal use:
#scrapy runspider scrpit_name.py

#para criar um projeto spyder inicial use:
# scrapy startprojec nome_projeto

#para criar um spider scraping dentro do projeto use:
# scrapy genspider scraping_nome_spider url_pagina




import scrapy

class Items(scrapy.Item):
    title_main=scrapy.Field()
    url=scrapy.Field()
    subject=scrapy.Field()
    title_subject=scrapy.Field()
    url_subject=scrapy.Field()
    
class gov_newsSpider(scrapy.Spider):
    name='Scraping Gov News'
    
    def __init__(self, tag=None):
        self.start_urls=['https://www.gov.br/pt-br/noticias']
        
    def parse(self, response):
        self.log(f'Accessing the URL: {response.url}')
        
        news = response.xpath('//div[@class="nitf-basic-tile tile-content"]')
        count=0
        self.log(f'Total of news: {len(news)}')
        
        for id_news in news:
            item = Items()
            count +=1
            
            item['title_main']=''.join(response.xpath('//title/text()').extract())
            item['url']=response.url
            item['subject']=' '.join(id_news.xpath('.//h2/a/text()').extract())
            item['title_subject']=''.join(id_news.xpath('.//p[@class="tile-subtitle"]/text()').extract())
            item['url_subject']=''.join(id_news.xpath('.//h2/a/@href').extract())
            
            yield item
            
        self.log(f'Scraped News: {count}')
        self.log('End of the scrapy')