from django.db import models

# Create your models here.

class Users(models.Model):
  username = models.CharField(max_length=50)


class Tweets(models.Model):
  message = models.CharField(max_length=140)
  pub_date = models.DateTimeField('date published')
  user = models.ForeignKey('Users')



