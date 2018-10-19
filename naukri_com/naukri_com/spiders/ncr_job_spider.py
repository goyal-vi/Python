import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from naukri_com.items import JobPost
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst 
from scrapy.loader.processors import MapCompose
import re

class DataAnalystJobsInNCR(CrawlSpider):
    name = 'data_analyst_jobs_in_ncr'
    allowed_domains = ['naukri.com']
    start_urls = ['https://www.naukri.com/data-analyst-jobs-in-ncr']
    pattern = re.compile(r"data-analyst-jobs-in-ncr-?[0-9]?")
    rules = (Rule(LinkExtractor(allow = [pattern]), callback = 'parse_page',follow = True),)
    def parse_page(self, response):
        job_list = response.css('.srp_container > .row')
        for job in job_list:
            job_loader = ItemLoader(JobPost(), selector = job)
            job_loader.default_input_processor = MapCompose(lambda x : x.strip())
            job_loader.default_output_processor = TakeFirst()
            job_loader.add_css('job_title','.content > ul > .desig::text')    
            job_loader.add_css('experience_required','.content > .exp::text')    
            job_loader.add_css('location','.content > .loc > span::text')    
            job_loader.add_css('company_name','.content > .orgRating > .org::text')    
            job_loader.add_css('job_description_url', 'div::attr(data-url)')    
            job_loader.add_css('key_skills','.content > .more > div[class = "desc"] >span[class = "skill"]::text')    
            job_loader.add_css('job_description','.content > .more > span[class = "desc"]::text')    
            job_loader.add_css('salary','.other_details > .salary::text')    
            job_loader.add_css('posted_by','.other_details > .rec_details > .rec_name::text')    
            job_loader.add_css('posted_on','.other_details > .rec_details > span[class = "date"]::text' )
            yield job_loader.load_item()    
             
