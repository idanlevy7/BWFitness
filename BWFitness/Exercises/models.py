from django.db import models
from django.urls import reverse
# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,null=False,unique=True)
    progressionTo = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='harder')
    progressionFrom = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='easier')
    difficulty = models.IntegerField()
    link = models.CharField(max_length=255,unique=True,null=True,blank=True)
    plane = models.CharField(max_length=255,null=True,blank=True)
    category = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('single',kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-difficulty','category']
