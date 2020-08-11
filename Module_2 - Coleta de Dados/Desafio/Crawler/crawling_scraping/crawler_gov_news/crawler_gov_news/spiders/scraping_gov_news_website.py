import scrapy
from crawler_gov_news.items import ScraperGovNewsItem

class ScrapingGovNewsWebsiteSpider(scrapy.Spider):
    name = 'scraping_gov_news_website'
    allowed_domains = ['https://www.gov.br/pt-br/noticias']
    start_urls = ['https://www.gov.br/pt-br/noticias/']
 
    def parse(self, response):
        self.log(f'Accessing the URL: {response.url}')
        
        news = response.xpath('//div[@class="nitf-basic-tile tile-content"]')
        count=0
        item = ScraperGovNewsItem()
        self.log(f'Total of news: {len(news)}')
        
        for id_news in news:
            count +=1
            
            item['title_main']=''.join(response.xpath('//title/text()').extract())
            item['url']=response.url
            item['subject']=' '.join(id_news.xpath('.//h2/a/text()').extract())
            item['title_subject']=''.join(id_news.xpath('.//p[@class="tile-subtitle"]/text()').extract())
            item['url_subject']=''.join(id_news.xpath('.//h2/a/@href').extract())
            
            yield item
            
        self.log(f'Scraped News: {count}')
        self.log('End of the scrapy')
