import scrapy
from crawler_gov_news.items import CrawlerGovNewsItem

class CrawlingGovNewsWebsiteSpider(scrapy.Spider):
    name = 'crawling_gov_news_website'
    allowed_domains = ['gov.br']
    start_urls = ['https://www.gov.br/pt-br/noticias/']

    def parse(self, response):
        
        self.log(f'Accessing the URL: {response.url}')
        
        item = CrawlerGovNewsItem()
        news = response.xpath('//div[@class="nitf-basic-tile tile-content"]')
                
        for id_news in news:
            url=''.join(id_news.xpath('.//h2/a/@href').extract()) #string
            yield response.follow(url, self.parse_news)
        
        item['url_page']=response.url
        yield item
            
    def parse_news(self, response):
        self.log(f'Accessing the URL: {response.url}')
        item = CrawlerGovNewsItem()       

        item['title_page']=''.join(response.xpath('//title/text()').extract())        
        item['subject_news']=''.join(response.xpath('//p[@class="nitfSubtitle"]//text()').extract()) 
        item['title_news']=''.join(response.xpath('//h1[@class="documentFirstHeading"]//text()').extract()) 
        item['subtitle_news']=''.join(response.xpath('//div[@class="documentDescription"]//text()').extract()) 
        item['text_news']=''.join(response.xpath('//div/div[@class=""]//text()').extract())
        item['author_news']=''.join(response.xpath('//div/div[@class=""]//span[@class="discreet"]//a/text()').extract())
        item['category_news']=''.join(response.xpath('//span[@class="contenttree-widget relationchoice-field"]//a/text()').extract())
        item['tags_news']=response.xpath('//div[@class="column"]//a[@class="link-category"]/text()').extract() 
        
        yield item