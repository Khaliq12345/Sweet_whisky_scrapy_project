#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy

class whisky(scrapy.Spider):
    name = 'sweet_whisky'
    allowed_domains = ['www.whiskyshop.com']
    start_urls = ['https://www.whiskyshop.com/flavour/sweet-whisky']
    custom_settings = {
       'FEED_URI' : 'tmp/whisky.csv'
   }
    
    def parse(self,response):
        for i in range(1,6):
            next_page = f'https://www.whiskyshop.com/flavour/sweet-whisky?p={i}'
            yield scrapy.Request(url = next_page,callback=self.parse_details)
            
    def parse_details(self,response):
        products = response.xpath("//li[@class='item product product-item']")
        for product in products:
            name = product.css('a.product-item-link::text').extract_first()
            price = product.css('span.price::text').extract_first()
            try:
                image = product.css('img.product-image-photo').attrib['src']
            except:
                image = 'None'
                
            scraped_info = {
                'Name':name,
                'Price':price,
                'Image':image
                }
            yield scraped_info

