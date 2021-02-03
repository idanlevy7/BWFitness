from django.db import models
from Exercises.models import Exercise
# Create your models here.

class Program(models.Model):
    exercise = models.OneToOneField(Exercise,on_delete=models.CASCADE,related_name='part_of_prog')

    def __str__(self):
        return self.exercise.name

    def get_absolute_url(self):
        return reverse('Exercise:single',kwargs={'slug': self.exercise.slug})
