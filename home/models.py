from django.db import models

# home models

# 1: opening model

class Openingone(models.Model):
    title = models.CharField(max_length=20)
    description1 = models.TextField(max_length=300)
    image = models.ImageField()
    event_word = models.CharField(max_length=20)
class Openingtow(models.Model):
    title = models.CharField(max_length=20)
    description1 = models.TextField(max_length=300)
    image = models.ImageField()
    event_word = models.CharField(max_length=20)
class Openingthree(models.Model):
    title = models.CharField(max_length=20)
    description1 = models.TextField(max_length=300)
    image = models.ImageField()
    event_word = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.title



# 2: our project model

class Projects(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.title
