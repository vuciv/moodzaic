from django.test import TestCase
from mood_model.models import Weights
from mood_model.sample_neural_network import MoodNeuralNetwork

# Create your tests here.

class WeightsTestCase(TestCase):
    def setUp(self):
        Weights.objects.create(username = "emil", password = "snibby")

class MoodNeuralNetworkTestCase(TestCase):
    def setUp(self):
        rand_weights = list(range(11))
        MoodNeuralNetwork.objects.create(weights = rand_weights)

    def test_feedforward(self):
        some_weights = list(range(11))
        network = MoodNeuralNetwork(some_weights)
        sample_data = [2,1,4,5,6,2,6,7,3,6,6]
        self.assertEqual(4, network.feedforward(sample_data))
        sample_data = [2,1,4,5,4,2,6,7,3,6,6]
        self.assertEqual(3.6, network.feedforward(sample_data))

    def test_activation(self):
        network = MoodNeuralNetwork()
        self.assertEqual(1, network.acivation(1))
        self.assertEqual(0.5, network.acivation(0.5))
        self.assertEqual(0, network.acivation(0))
        self.assertEqual(-.5, network.acivation(-.5))
        self.assertEqual(-100, network.acivation(0))

    def test_deriv_activation(self):
        network = MoodNeuralNetwork()
        self.assertEqual(0, network.deriv_acivation(1))
        self.assertEqual(0.5, network.deriv_acivation(0.5))
        self.assertEqual(1, network.deriv_acivation(0))
        self.assertEqual(-.5, network.deriv_acivation(-.5))
        self.assertEqual(-1, network.deriv_acivation(0))

    def test_loss(y_true, y_pred):
        network = MoodNeuralNetwork()
        sample_data = list(range(100))
        sample_real = list(range(0,100)) + 0.1
        self.assertEqual(1, network.loss(sample_data, sample_real))
        sample_real = list(range(0,100))
        self.assertEqual(0, network.loss(sample_data, sample_real))

    def test_train(y_true, y_pred):
        some_weights = list(range(11))
        network = MoodNeuralNetwork(sample_weights)
        sample_data = [2,1,4,5,6,2,6,7,3,6,6]
        true = 3.5
        prediction = network.feedforward(sample_data)
        loss1 = network.loss(true, prediction)
        network.train()
        prediction = network.feedforward(sample_data)
        loss2 = network.loss(true, prediction)
        self.assertTrue(lass2 < loss1)
