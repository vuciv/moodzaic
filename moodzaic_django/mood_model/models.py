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

    def getWeeklyData(self, obs, user_observations):
        today = obs.date.today()
        week_ago = today - datetime.timedelta(days=7)
        weekly_data = user_observations.objects.filter(date__gte=week_ago,date__lte=today)

        days_with_obs = weekly_data.__len__

        if days_with_obs:
            return 0, 0
        
        exercise_sum = 0
        work_sum = 0
        for past_obs in weekly_data.iterator():
            exercise_sum += past_obs.exercise
            work_sum += past_obs.work
        
        return exercise_sum / days_with_obs, work_sum / days_with_obs


    def transformUserData(self):

        profile = self.user.profile
        user_observations = Observation.objects.filter(profile__user__name=profile.user.username)
        user_observations = user_observations.objects.order_by("date")
        
        array = []
        for obs in user_observations.iterator():
            weekly_exercise, weekly_work = self.getWeeklyData(obs)
            
            row = [
                obs.sleep, 
                obs.exercise, 
                weekly_exercise,
                obs.meals, 
                
                obs.work,
                weekly_work
            ]
            array.append(row)

        return np.array(array)


    def delimiterToList(self, string_list, key):
        return string_list.split(',')
    
    def listToDelimiter(self, l, expected_size):
        if len(l) != expected_size:
            raise ValueError
        return ",".join(l)

    def retrain(self):

        weights = self.delimiterToList(self.weights_int_list, "weight")
        biases = self.delimiterToList(self.bias_int_list, "bias")

        """
        model = MoodNeuralNetwork(weights=weights, biases=biases)
        input_data = self.transformUserData()
        model.train(input_data)

        self.setWeightsWeights(self.listToDelimiter(model.getWeights), 208)
        self.setWeightsBias(self.listToDelimiter(model.getBiases), 21)


        #self.user.profile.setNotifications()
        """

    

    def setWeightsUser(self, user):
        pass

    def setWeightsWeights(self, weights_dict):
        


        pass

    def setWeightsBias(self, biases_dict):
        pass
