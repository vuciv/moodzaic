from django.db import models
<<<<<<< HEAD
from users.models import User
from django.core.validators import int_list_validator 
=======
>>>>>>> master

#from mood_model.sample_neural_network import MoodNeuralNetwork


class Weights(models.Model):

    # ...
    user = models.OneToOneField(
<<<<<<< HEAD
        User, 
        unique=True, 
        related_name='weights',
        on_delete='models.CASCADE',
        null=True
    )

    weights_int_list = models.TextField(
        validators=[int_list_validator],
        default=""
    )
    bias_int_list = models.TextField(
        validators=[int_list_validator],
        default=""
    )

    
    def predict(self):
=======
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

>>>>>>> master

        pass

    def retrain(self):

        pass


<<<<<<< HEAD

        


    




=======
    class Meta:
        db_table = 'weights'
        managed = False
>>>>>>> master
