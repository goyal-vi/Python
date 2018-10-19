# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

class NullValueHandlerPipeline(object):
    def process_item(self, item, spider):
        attributes = ["job_title", "experience_required", "location", "company_name", "job_description", "key_skills", "job_description_url", "salary", "posted_on", "posted_by"]
        for attr in attributes:
            try:
                item[attr]
            except KeyError:
                item[attr] = ""
        return item

#class CalculatorPostedOn(object):
#    def process_item(self, item, spider):
#        today_date = datetime.datetime.today()
#        if item['posted_on']:
#               value = item['posted_on'][0]
#               if 'day' in value:
#                   num = int(value.split()[0])
#                   item['posted_on'][0] = today_date - datetime.timedelta(days = num)    
