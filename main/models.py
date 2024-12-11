from django.db import models
from users.models import CustomUser

# Create your models here.

class Exercice (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True)
    author_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

class Training(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True)
    author_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    exercices = models.ManyToManyField(Exercice, through="Approach", related_name="trainigs")

class TrainingProdram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True)
    author_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

class Approach(models.Model):
    training_id = models.ForeignKey(Training,  on_delete=models.CASCADE)
    exercice_id = models.ForeignKey(Exercice,  on_delete=models.CASCADE)
    approach_order = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField(null=True)
    
class Schedule(models.Model):
    DAY_OF_WEEK_CHOICES = [
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье'),
    ]
    program_id = models.ForeignKey(TrainingProdram, on_delete=models.CASCADE)
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES)
    time = models.TimeField()