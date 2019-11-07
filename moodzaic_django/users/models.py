from django.db import models

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
        return 'not false'

    def setGoalFrequency(self, frequency):
        #TODO
        return 'not false'

    def setGoalTime(self, time):
        #TODO
        return 'not false'

class Profile(models.Model):
    ProgressScore = models.IntegerField(default=0)

    def getProgressScore(self):
        return self.ProgressScore

    def setProgressScore(self, ProgressScore):
        self.ProgressScore = ProgressScore

    def ProgressScore_calc(self, goals, observations):
        #TODO
        #goals: list of goals
        #observations: list of observations
        return

    def make_goal_post(self, goal, post):
        ## TODO:
        #goal: goal
        #post: str
        return

    def make_post(self, post):
        ## TODO
        #post: str
        return

    def set_mood(self, mood):
        ##TODO : mood is int
        return

 class Observation(models.Model):
     activity = models.CharField()
     date = models.DateTimeField('date observed')
     sleep = models.FloatField(default=-1)
     exercise_24hr = models.FloatField(default = -1)
     meals_24hr = models.IntegerField(default=-1)
     work_24hr = models.FloatField(default=-1)

 class Mood(models.Model):
     name = models.CharField()
     mood = models.FloatField(default=-1)
