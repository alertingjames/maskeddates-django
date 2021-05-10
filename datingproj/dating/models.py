from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=50)
    email=models.CharField(max_length=80)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=5)
    fb_photo = models.CharField(max_length=500)
    photo_url = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    answers = models.CharField(max_length=1000)
    answers2 = models.CharField(max_length=1000)
    premium = models.CharField(max_length=10)
    photos = models.CharField(max_length=1000)
    photo_unlock = models.CharField(max_length=10)
    selfie_approved = models.CharField(max_length=10)
    last_login = models.CharField(max_length=50)
    actives = models.CharField(max_length=11)
    phone_imei = models.CharField(max_length=100)

class Post(models.Model):
    user_id = models.CharField(max_length=11)
    photo = models.CharField(max_length=1000)
    text = models.CharField(max_length=1000)
    datetime = models.CharField(max_length=30)

class Notification(models.Model):
    user_id = models.CharField(max_length=11)
    sender_id = models.CharField(max_length=11)
    sender_name = models.CharField(max_length=50)
    sender_email=models.CharField(max_length=80)
    sender_photo = models.CharField(max_length=500)
    notitext = models.CharField(max_length=500)
    notitime = models.CharField(max_length=30)
    enteredtime = models.CharField(max_length=30)
    exitedtime = models.CharField(max_length=30)
    unraveled = models.CharField(max_length=5)
    option = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    active = models.CharField(max_length=5)

class Unravel(models.Model):
    me_id = models.CharField(max_length=11)
    user_id = models.CharField(max_length=11)
    unraveled = models.CharField(max_length=5)
    entered_datetime = models.CharField(max_length=30)
    exited_datetime = models.CharField(max_length=30)
    active = models.CharField(max_length=5)

class Answer(models.Model):
    me_id = models.CharField(max_length=11)
    user_id = models.CharField(max_length=11)
    icebreaker = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    datetime = models.CharField(max_length=30)

class Dynamical(models.Model):
    dynamical_question = models.CharField(max_length=1000)

class Plan(models.Model):
    months = models.CharField(max_length=5)
    dates = models.CharField(max_length=5)
    price = models.CharField(max_length=5)
    months1 = models.CharField(max_length=5)
    dates1 = models.CharField(max_length=5)
    price1 = models.CharField(max_length=5)
    months2 = models.CharField(max_length=5)
    dates2 = models.CharField(max_length=5)
    price2 = models.CharField(max_length=5)
    months3 = models.CharField(max_length=5)
    dates3 = models.CharField(max_length=5)
    price3 = models.CharField(max_length=5)

class Bid(models.Model):
    user_id = models.CharField(max_length=11)
    folder_id = models.CharField(max_length=11)
    caption = models.CharField(max_length=100)
    text = models.CharField(max_length=5000)

class Folder(models.Model):
    user_id = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    files = models.CharField(max_length=11)

class File(models.Model):
    folder_id = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=1000)

class Picture(models.Model):
    member_id = models.CharField(max_length=11)
    picture_url = models.CharField(max_length=1000)

class Note(models.Model):
    user_id = models.CharField(max_length=11)
    caption = models.CharField(max_length=100)
    text = models.CharField(max_length=5000)

class Settings(models.Model):
    member_email = models.CharField(max_length=80)
    min_age = models.CharField(max_length=5)
    max_age = models.CharField(max_length=5)
    profile = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)












