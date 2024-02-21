from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="新发布",
    )
    def was_pubished_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # models.
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=datetime.date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline


class Person(models.Model):
    name = models.CharField(max_length=20)
    office_tel = models.CharField(max_length=20)
    cellpone_number = models.CharField(max_length=20)


class AskForLeave(models.Model):
    def timeoffset():
        nowtime = datetime.datetime.now
        offset = datetime.timedelta(hours=4.0)
        # retime = (nowtime + offset).strftime("%Y-%m-%d %H:%M:%S")
        retime = nowtime + offset
        return retime

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.datetime.now)
    back_time = models.DateTimeField(default=timeoffset)
    place = models.CharField(max_length=200)

    def __str__(self):
        return self.person.name
