from django.db import models
from django.utils.text import slugify
# questions list

class Questions(models.Model):
    image = models.ImageField(upload_to='comp')
    name = models.CharField(max_length=40)
    question = models.CharField(max_length=400)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs ):
           ##logic
       self.slug = slugify(self.name)
       super(Questions,self).save(*args, **kwargs) 
    
    def __str__(self):
       return self.question


# answer

class Answer(models.Model):
    name= models.CharField(max_length=30)
    email = models.EmailField()
    number = models.CharField(max_length=14)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer = models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name,self.question.name}"