from django.db import models


class MyNews(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=40, blank=False)
    Description = models.TextField(max_length=10000)
    publication_date = models.DateField()



class Topic:
    name = models.CharField(max_length=10)