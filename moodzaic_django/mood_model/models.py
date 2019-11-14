import datetime

from django.core.validators import int_list_validator
from django.db import models
import numpy as np

from users.models import User, Observation
from mood_model.mood_neural_network import MoodNeuralNetwork


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

    def getData(self, obs, observations, timeframe):
        today = obs.date.today()
        week_ago = today - datetime.timedelta(days=timeframe)
        weekly_data = observations.objects.filter(date__gte=week_ago, date__lte=today)

        days_with_obs = weekly_data.__len__

        if days_with_obs == 0:
            return 0, 0

        exercise_sum, work_sum = 0, 0

        for past_obs in weekly_data.iterator():
            exercise_sum += past_obs.exercise
            work_sum += past_obs.work

        return exercise_sum / days_with_obs, work_sum / days_with_obs


    def transformUserData(self, timeframe):
        profile = self.user.profile
        observations = Observation.objects.filter(user__user__username=profile.user.username)
        observations = observations.order_by("date")

        input_data = []
        mood_data = []
        for obs in observations.iterator():
            weekly_exercise, weekly_work = self.getData(obs, observations, timeframe)

            row = [
                obs.sleep, obs.exercise, weekly_exercise, obs.meals,
                0, 0, 0, 0, 0, # goals, goals completed, goals missed, goals ratio, past mood score
                obs.work, weekly_work
            ]
            input_data.append(row)
            mood_data.append(obs.mood.mood)
        return np.array(input_data), np.array(mood_data)


    def retrain(self):

        weights = self.weights_int_list.split(',')
        biases = self.bias_int_list.split(',')

        model = MoodNeuralNetwork(weights=weights, biases=biases)
        input_data, mood_data = self.transformUserData(7)
        model.train(input_data, mood_data)

        weightDict = model.getWeights()
        weights = []
        for i in range(len(weightDict)):
            weights.append(weightDict["weight" + str(i)])
        self.setWeightsWeights(weights)

        biasDict = model.getBiases()
        biases = []
        for i in range(len(biasDict)):
            weights.append(biasDict["weight" + str(i)])
        self.setWeightsBias(biases)

        return True

    def predict(self):
        weights = self.weights_int_list.split(',')
        biases = self.bias_int_list.split(',')
        model = MoodNeuralNetwork(weights=weights, biases=biases)
        input_data, mood_data = self.transformUserData(1)
        outout = model.feedforward(input_data)
        mood = model.roundClass(output)
        return mood
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
