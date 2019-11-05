from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=9)

    def setUserUsername(self, username):
        #TODO
        return 'not false'
    
    def setUserPassword(self, password):
        #TODO
        return 'not false'
    
    def setUserAge(self, age):
        #TODO
        return 'not false'
    
    def setUserGender(self, age):
        #TODO
        return 'not false'

class Goal(models.Model):
    goal = models.CharField(max_length=30)
    frequency = models.IntegerField(default=1)
    time = models.TimeField()

    def setGoalGoal(self, goal):
        #TODO
        return
    
    def setGoalFrequency(self, frequency):
        #TODO
        return
    
    def setGoalTime(self, time):
        #TODO
        return