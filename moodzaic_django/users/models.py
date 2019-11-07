from django.db import models
from datetime import date

class User(models.Model):
    username = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=20, default='')
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=9, default='')

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
    time = models.CharField(max_length=10)

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
     name = models.CharField(max_length=20, default="")
     mood = models.FloatField(default=-1)
     #date = models.DateField('date observed', auto_now_add=True, blank=True)
     #make list of moods that will be kept track of
     def getName(self):
         #TODO
         return

     def setName(self, name):
        #TODO
        return

     def getMood(self):
        #TODO
        return

     def setMood(self, mood):
        ## TODO:
        return

class Profile(models.Model):
    ProgressScore = models.IntegerField(default=0)
    #reminderList = models.ListCharField(base_field=CharField, size=None)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True
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


    def getUser(self):
        ## TODO:
        return


class Observation(models.Model):
    date = models.DateField('date observed', auto_now_add=True, blank=True)
    sleep = models.FloatField(default=-1)
    exercise = models.FloatField(default = -1)
    meals = models.IntegerField(default=-1)
    work = models.FloatField(default=-1)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    mood = models.OneToOneField(
        Mood,
        on_delete=models.CASCADE,
        null=True
    )


    def setSleep(self, hours):
        ## TODO:
        return


    def setExercise(self, hours):
        ## TODO:
        return


    def setMeals(self, num):
        ## TODO:
        return


    def setWork(self, hours):
        ## TODO:
        return

    def setMood(self, mood_str, mood_int):
        ## TODO:
        return
