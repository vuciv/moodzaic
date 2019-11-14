from django.db import models
from datetime import date
from django.contrib.auth.models import User
from datetime import datetime

#from community.models import Community

'''
class User(models.Model):
    username = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=20, default='')
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=9, default='')

    def setUserUsername(self, username):
        if not (isinstance(username, 'str')):
            return False
        if len(username) > 20:
            return False
        self.username = username
        self.save()
        return True

    def setUserPassword(self, password):
        if not (isinstance(password, 'str')):
            return False
        if len(password) > 20:
            return False
        self.password = password
        self.save()
        return True

    def setUserAge(self, age):
        #TODO
        return 'not false'

    def setUserGender(self, age):
        #TODO
        return 'not false'
'''

class Goal(models.Model):
    goal = models.CharField(max_length=30)
    frequency = models.IntegerField(default=1)
    time = models.TimeField()

    def setGoalGoal(self, goal):
        if not (isinstance(goal, type('str'))):
            return False
        if len(goal) > 30:
            return False
        self.goal = goal
        self.save()
        return True

    def setGoalFrequency(self, frequency):
        if not (isinstance(frequency, 'int')):
            return False
        self.frequency = frequency
        self.save()
        return True

    def setGoalTime(self, time_string):
        try:
            time = datetime.strptime(time_string, '%H:%M').time()
            self.time = time
            self.save()
        except Exception as e:
            print(e)
            return False

class Mood(models.Model):
     name = models.CharField(max_length=20, default="")
     mood = models.IntegerField(default=-1)
     #date = models.DateField('date observed', auto_now_add=True, blank=True)
     #make list of moods that will be kept track of

     def setName(self, name):
        if not (isinstance(name, type('a'))):
            return False
        if len(name) < 20:
            self.name = name
            self.save()
            return True
        else:
            return False

     def setMood(self, mood):
        if not (isinstance(mood, type(2))):
            return False
        if mood >= 0:
            self.mood = mood
            self.save()
            return True
        else:
            return False

class Profile(models.Model):
    ProgressScore = models.IntegerField(default=0)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=9, default='')
    #reminderList = models.ListCharField(base_field=CharField, size=None)
    username = models.CharField(max_length=150, default='')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='profile'
    )

    def getProgressScore(self):
        return self.ProgressScore

    def setProgressScore(self, ProgressScore):
        self.ProgressScore = ProgressScore
        self.save()

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
        if hours  >= 0 and hours <= 24:
            self.sleep = hours
            return True
        else:
            return False


    def setExercise(self, hours):
        if hours  >= 0 and hours <= 24:
            self.exercise = hours
            return True
        else:
            return False

    def setMeals(self, num):
        if num  >= 0:
            self.meals = num
            return True
        else:
            return False


    def setWork(self, hours):
        if hours  >= 0 and hours <= 24:
            self.work = hours
            return True
        else:
            return False

    def setMood(self, mood_str, mood_int):
        self.mood.setMood(mood_int)
        self.mood.setName(mood_str)
        self.save()
        return True
