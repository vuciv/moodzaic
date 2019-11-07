from django.db import models
from users.models import User

class ObservationWeights(models.Model):

    # ...
    user = models.OneToOneField(
        User, 
        unique=True, 
        related_name='weight',
        on_delete='models.CASCADE'
    )
    sleep = models.FloatField(default=1)
    daily_exercise = models.FloatField(default=1)
    weekly_exercise = models.FloatField(default=1)
    daily_work = models.FloatField(default=1)
    weekly_work = models.FloatField(default=1)
    daily_meals = models.IntegerField(default=1)
    past_mood = models.FloatField(default=1)


    class Meta:
        db_table = 'weights'
        managed = False
    

class GoalWeights(models.Model):

    goals_completed = models.IntegerField(default=0)
    goals_missed = models.IntegerField(default=0)
    existing_goals = models.IntegerField(default=0)



    class Meta:
        db_table = 'weights'
        managed = False



    




