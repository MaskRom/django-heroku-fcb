from django.db import models

class ClassDB(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

class ShortcutURL(models.Model):
    post = models.ForeignKey(ClassDB, related_name='shortcutURL', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField()

class Info(models.Model):
    post = models.ForeignKey(ClassDB, related_name='info', on_delete=models.CASCADE)
    head = models.CharField(max_length= 255)
    body = models.CharField(max_length= 2000)
    posted_date = models.DateTimeField(auto_now=True)
    posted_name = models.CharField(max_length = 20)

class Timetable(models.Model):
    post = models.ForeignKey(ClassDB, related_name='timetable', on_delete=models.CASCADE)
    mon_1st = models.CharField(max_length= 255)
    mon_1st_sub = models.CharField(max_length= 255)
    mon_2st = models.CharField(max_length= 255)
    mon_2st_sub = models.CharField(max_length= 255)
    mon_3st = models.CharField(max_length= 255)
    mon_3st_sub = models.CharField(max_length= 255)

    tue_1st = models.CharField(max_length= 255)
    tue_1st_sub = models.CharField(max_length= 255)
    tue_2st = models.CharField(max_length= 255)
    tue_2st_sub = models.CharField(max_length= 255)
    tue_3st = models.CharField(max_length= 255)
    tue_3st_sub = models.CharField(max_length= 255)

    wed_1st = models.CharField(max_length= 255)
    wed_1st_sub = models.CharField(max_length= 255)
    wed_2st = models.CharField(max_length= 255)
    wed_2st_sub = models.CharField(max_length= 255)
    wed_3st = models.CharField(max_length= 255)
    wed_3st_sub = models.CharField(max_length= 255)

    thu_1st = models.CharField(max_length= 255)
    thu_1st_sub = models.CharField(max_length= 255)
    thu_2st = models.CharField(max_length= 255)
    thu_2st_sub = models.CharField(max_length= 255)
    thu_3st = models.CharField(max_length= 255)
    thu_3st_sub = models.CharField(max_length= 255)

    fri_1st = models.CharField(max_length= 255)
    fri_1st_sub = models.CharField(max_length= 255)
    fri_2st = models.CharField(max_length= 255)
    fri_2st_sub = models.CharField(max_length= 255)
    fri_3st = models.CharField(max_length= 255)
    fri_3st_sub = models.CharField(max_length= 255)