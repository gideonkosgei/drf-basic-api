# basic_api/models.py
from django.db import models
#list
Grade = [
    ('excellent', 1),
    ('average', 0),
    ('bad', -1)
]


Country = [
    ('kenya', 0),
    ('uganda', 1),
    ('tanzania', 2)
]

# DataFlair
class DRFPost(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    uploaded = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = Grade, default = 'average', max_length = 50)
    class Meta:
        ordering = ['uploaded']
    def __str__(self):
        return self.name


class DRFUser(models.Model):
    firstName = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    age = models.CharField(max_length = 100)
    telephone = models.CharField(max_length = 100)
    country = models.CharField(choices = Country, default = 'kenya', max_length = 50)
    class Meta:
        ordering = ['firstName']
    def __str__(self):
        return self.firstName        