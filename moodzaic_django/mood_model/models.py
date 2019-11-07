from django.db import models
from users.models import User
from django.core.validators import int_list_validator 

#from mood_model.sample_neural_network import MoodNeuralNetwork


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


    def retrain(self):
        pass

    def setWeightsUser(self, User):
        pass

    def setWeightsWeights(self, weight_list):
        pass

    def setWeightsBias(self, bias_list):
        pass
