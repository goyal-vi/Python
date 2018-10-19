# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import MapCompose
from datetime import datetime,timedelta

def to_date(string):
    string = str(string)
    today = datetime.today()	
    if len(string) > 0 and string != 'Today' and string != 'today' and 'day' in string:
        num = int(string.split()[0])
        temp =  today - timedelta(days = num)
        return str(temp.date())
    elif len(string) > 0:
        return str(today.date())
    else:
        return ""     	

class JobPost(scrapy.Item):
    job_title = scrapy.Field()
    experience_required = scrapy.Field()
    location = scrapy.Field()
    company_name = scrapy.Field()
    job_description_url = scrapy.Field()
    key_skills = scrapy.Field()
    job_description = scrapy.Field()
    salary = scrapy.Field()
    posted_by = scrapy.Field()
    posted_on = scrapy.Field(input_processor = MapCompose(to_date))
