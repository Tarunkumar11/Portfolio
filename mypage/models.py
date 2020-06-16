from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 50)
    message = models.CharField(max_length = 150)
    def __str__(self):
        return self.Name
class resume(models.Model):
    fileres = models.FileField()
    class Meta:
        verbose_name_plural = "My_resume"
    def __str__(self):
        return self.fileres.name
