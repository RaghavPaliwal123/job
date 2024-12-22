import scrapy
import requests

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = ['https://example.com/jobs']

    def parse(self, response):
        jobs = response.css('job_selector')
        for job in jobs:
            job_data = {
                'title': job.css('title_selector::text').get(),
                'company_name': job.css('company_selector::text').get(),
                'location': job.css('location_selector::text').get(),
                'employment_type': job.css('employment_selector::text').get(),
                'posted_date': job.css('posted_selector::text').get(),
                'description': job.css('description_selector::text').get(),
                'url': job.css('url_selector::attr(href)').get(),
            }
            # Post data to Django backend
            requests.post('http://127.0.0.1:8000/jobs/add/', data=job_data)

        next_page = response.css('pagination_selector::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
