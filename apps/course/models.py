from __future__ import unicode_literals
from ..logreg.models import User
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    user = models.ManyToManyField(User, related_name="user")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Location(models.Model):
    location = models.CharField(max_length=100)
    course = models.ManyToManyField(Course, related_name="course")
