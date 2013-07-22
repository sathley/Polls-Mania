from django.db import models

# Create your models here.


class Polls(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(name='date published')


class Choices(models.Model):
    choice_text = models.CharField(max_length=200)
    poll = models.ForeignKey(Polls)
    votes = models.IntegerField(default=0)


