from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50)
    posted_date = models.DateTimeField()
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
