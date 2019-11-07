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
