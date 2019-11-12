from django.core.validators import int_list_validator 
import numpy as np

from django.db import models
from users.models import User, Observation

import datetime

from mood_model.sample_neural_network import MoodNeuralNetwork


class Weights(models.Model):

    # ...
    user = models.OneToOneField(
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

    def getWeeklyData(self, obs, observations):
        today = obs.date.today()
        week_ago = today - datetime.timedelta(days=7)
        weekly_data = observations.objects.filter(date__gte=week_ago, date__lte=today)

        days_with_obs = weekly_data.__len__

        if days_with_obs == 0:
            return 0, 0
        
        exercise_sum, work_sum = 0, 0

        for past_obs in weekly_data.iterator():
            exercise_sum += past_obs.exercise
            work_sum += past_obs.work
        
        return exercise_sum / days_with_obs, work_sum / days_with_obs


    def transformUserData(self):

        profile = self.user.profile
        observations = Observation.objects.filter(user__user__username=profile.user.username)
        observations = observations.order_by("date")
        
        input_data = []
        mood_data = []
        for obs in observations.iterator():
            weekly_exercise, weekly_work = self.getWeeklyData(obs, observations)
            
            row = [
                obs.sleep, obs.exercise, weekly_exercise, obs.meals,
                
                obs.work, weekly_work
            ]
            input_data.append(row)
            mood_data.append(obs.mood.mood / obs.mood.moods.size)
        return np.array(input_data), np.array(mood_data)
            

    def retrain(self):

        weights = self.weights_int_list.split(',')
        biases = self.bias_int_list.split(',')

        
        model = MoodNeuralNetwork(weights=weights, biases=biases)
        input_data, mood_data = self.transformUserData()
        model.train(input_data, mood_data)

        # self.setWeightsWeights(model.getWeights())
        # self.setWeightsBias(model.getBiases())


        #self.user.profile.setNotifications()
        
    def setWeightsUser(self, user):
        if self.user is not None:
            return False
        
        self.user = user
        return True

    def setWeightsWeights(self, weights_list):
        if len(weights_list) != 208:
            return False
        
        self.weights_int_list = ",".join(str(x) for x in weights_list)
        return True

    def setWeightsBias(self, biases_list):
        if len(biases_list) != 21:
            return False
        self.bias_int_list = ",".join(str(x) for x in biases_list)
        return True

