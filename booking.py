import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urljoin

class BookingSpider(scrapy.Spider):
    name = "booking"

    def start_requests(self):
        # Put the urls for the best 5 destinations to go we found earlier
        start_urls =['https://www.booking.com/searchresults.fr.html?ss=Lille',
                     'https://www.booking.com/searchresults.fr.html?ss=Nîmes',
                     'https://www.booking.com/searchresults.fr.html?ss=Saint-Malo',
                     'https://www.booking.com/searchresults.fr.html?ss=Uzes',
                     'https://www.booking.com/searchresults.fr.html?ss=Paris']
        
        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse_hotel_list)

    # First method to scrap the urls of the hotels
    def parse_hotel_list(self, response):
        links = response.xpath('//*[@id="search_results_table"]/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a/@href').getall()

        for hotel in links[:20]: # Select only the first 20 hotels
            hotel_link = urljoin(response.url, hotel)
            yield scrapy.Request(url=hotel_link, callback=self.parse_hotel_details)

    # Second method to scrap a hotel detailed information
    def parse_hotel_details(self, response):
        hotel_details = response.xpath('//*[@id="basiclayout"]/div')
        for info in hotel_details:
            yield{
                "hotel_name" : info.xpath('//*[@id="hp_hotel_name"]/div/h2/text()').get(),
                "url": response.url,
                "coord_gps" : info.xpath('//*[@id="hotel_header"]').attrib["data-atlas-latlng"],
                "rate" : info.xpath('//*[@id="js--hp-gallery-scorecard"]/a/div/div/div/div[1]/text()').get(),
                "description_1" : info.xpath('//*[@id="property_description_content"]/text()').getall(),
                "description_2" : info.xpath('//*[@id="property_description_content"]/p/text()').getall()
            }

filename = "hotels.json"

if filename in os.listdir('results/'):
        os.remove('results/' + filename)

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'results/' + filename : {"format": "json"},
    }
})

process.crawl(BookingSpider)
process.start()