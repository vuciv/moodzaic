from django.db import models
from datetime import date

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
    time = models.DateTimeField()

    def setGoalGoal(self, goal):
        #TODO
        return 'not false'

    def setGoalFrequency(self, frequency):
        #TODO
        return 'not false'

    def setGoalTime(self, time):
        #TODO
        return 'not false'



class Mood(models.Model):
     name = models.CharField(max_length=20)
     mood = models.FloatField(default=-1)
     date = models.DateField('date observed', auto_now_add=True, blank=True)
     #make list of moods that will be kept track of

class Profile(models.Model):
    ProgressScore = models.IntegerField(default=0)
    reminderList = models.ListCharField(base_field=CharField, size=None)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def getProgressScore(self):
        return self.ProgressScore

    def setProgressScore(self, ProgressScore):
        self.ProgressScore = ProgressScore

    def ProgressScoreCalc(self, goals, observations):
        #TODO
        #goals: list of goals
        #observations: list of observations
        return

    def makeGoalPost(self, goal, post):
        ## TODO:
        #goal: goal
        #post: str
        return

    def makePost(self, post):
        ## TODO
        #post: str
        return

    def setMood(self, mood):
        ##TODO : mood is int
        return

class Observation(models.Model):
    date = models.DateField('date observed', auto_now_add=True, blank=True)
    sleep = models.FloatField(default=-1)
    exercise_24hr = models.FloatField(default = -1)
    meals_24hr = models.IntegerField(default=-1)
    work_24hr = models.FloatField(default=-1)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mood = models.OneToOneField(
        Mood,
        on_delete=models.CASCADE,
    )
