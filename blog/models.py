from django.db import models
from django.utils.text import slugify
# blog

class Blog(models.Model):
    Name = models.CharField(max_length=30)
    Image = models.ImageField()
    Title = models.CharField(max_length=300)
    Description = models.TextField()
    Slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs ):
           ##logic
       self.Slug = slugify(self.Name)
       super(Blog,self).save(*args, **kwargs) 
    
    
    def __str__(self):
        return self.Name