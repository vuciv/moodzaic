from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=9)

    def setUsername(self, username):
        self.username = username
        return
    
    def getUsername(self):
        return self.username