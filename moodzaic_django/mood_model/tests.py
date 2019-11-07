from django.test import TestCase
from mood_model.models import ObservationWeights, GoalWeights
from mood_model.sample_neural_network import MoodNeuralNetwork

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username = "emil", password = "snibby")
