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
        network = MoodNeuralNetwork(weights = rand_weights)

    def test_feedforward(self):
        some_weights = list(range(11))
        network = MoodNeuralNetwork(some_weights)
        sample_data = [2,1,4,5,6,2,6,7,3,6,6]
        self.assertEqual(4, network.feedforward(sample_data))
        sample_data = [2,1,4,5,4,2,6,7,3,6,6]
        self.assertEqual(3.6, network.feedforward(sample_data))

    def test_activation(self):
        network = MoodNeuralNetwork()
        self.assertEqual(1, network.activation(1))
        self.assertEqual(0.5, network.activation(0.5))
        self.assertEqual(0, network.activation(0))
        self.assertEqual(-.5, network.activation(-.5))
        self.assertEqual(-100, network.activation(0))

    def test_deriv_activation(self):
        network = MoodNeuralNetwork()
        self.assertEqual(0, network.deriv_activation(1))
        self.assertEqual(0.5, network.deriv_activation(0.5))
        self.assertEqual(1, network.deriv_activation(0))
        self.assertEqual(-.5, network.deriv_activation(-.5))
        self.assertEqual(-1, network.deriv_activation(0))

    def test_loss(self):
        network = MoodNeuralNetwork()
        sample_data = list(range(100))
        sample_real = [x + 0.1 for x in list(range(0,100))]
        self.assertEqual(1, network.loss(sample_data, sample_real))
        sample_real = list(range(0,100))
        self.assertEqual(0, network.loss(sample_data, sample_real))

    def test_train(self):
        some_weights = list(range(11))
        network = MoodNeuralNetwork(some_weights)
        sample_data = [2,1,4,5,6,2,6,7,3,6,6]
        true = 3.5
        prediction = network.feedforward(sample_data)
        loss1 = network.loss(true, prediction)
        network.train(sample_data, [true])
        prediction = network.feedforward(sample_data)
        loss2 = network.loss(true, prediction)
        self.assertTrue(loss2 < loss1)
