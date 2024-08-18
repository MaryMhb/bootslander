from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    email = models.EmailField (null=True)
    password = models.IntegerField()
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.username