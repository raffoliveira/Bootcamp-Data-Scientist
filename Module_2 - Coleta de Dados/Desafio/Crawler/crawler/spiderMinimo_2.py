#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:46:58 2020

@author: rafael
"""

import scrapy

class SpiderMinimo(scrapy.Spider):

    """Scrapy spider mínimo"""
    name = 'minimo'
    
    def start_requests(self):
        url='https://www.gov.br/pt-br/noticias'
        return [scrapy.Request(url)]
    
    def parse(self, response):
        self.log(f'Acessando a URL: {response.url}')