from pyexpat import model
from turtle import done, title
from django.db import models

class Task(models.Model):

    STATUS = (
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    created_al = models.DateTimeField(auto_now_add=True)
    Uptade_al = models.DateTimeField(auto_now = True)

    def __str__(self):
       return self.title