from django.test import TestCase
from mood_model.models import Weights
from users.models import User, Profile
from mood_model.sample_neural_network import MoodNeuralNetwork

# Create your tests here.

# Testing the weights stored in the django database, and its functions
class WeightsTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1", password="password1")
        user2 = User.objects.create(username="user2", password="password2")

        Profile.objects.create(user=user1)

        Weights.objects.create(
            user=User.objects.get(username="user1"),
            weights_int_list=','.join(["1"] * 208),
            bias_int_list=','.join(["1"] * 21)
        )
        Weights.objects.create()


    def test_setWeightsUserSuccess(self):
        testWeights = Weights.objects.last()
        old_user = testWeights.user
        new_user = User.objects.get(username="user2")
        testWeights.setWeightsUser(new_user)
        self.assertEqual(testWeights.user, new_user)
        self.assertNotEqual(testWeights.user, old_user)

    def test_setWeightsUserFailure(self):
        testWeights = Weights.objects.first()
        old_user = testWeights.user
        new_user = User.objects.get(username="user2")
        testWeights.setWeightsUser(new_user)
        self.assertEqual(testWeights.user.username, old_user.username)
        self.assertNotEqual(testWeights.user.username, new_user.username)


    def test_setWeightsWeightsSuccess(self):
        testWeights = Weights.objects.first()
        old_weights = testWeights.weights_int_list
        new_weights = [0] * 208
        self.assertTrue(testWeights.setWeightsWeights(new_weights))
        self.assertEqual(testWeights.weights_int_list, ",".join("0" * 208))
        self.assertNotEqual(testWeights.weights_int_list, old_weights)

    def test_setWeightsWeightsFailureWrongWeightCount(self):
        testWeights = Weights.objects.first()
        old_weights = testWeights.weights_int_list
        new_weights = [1] * 207
        self.assertFalse(testWeights.setWeightsWeights(new_weights))
        self.assertNotEqual(testWeights.weights_int_list,",".join("1" * 207))
        self.assertEqual(testWeights.weights_int_list, old_weights)

    def test_setWeightsWeightsFailureWrongFormat(self):
        testWeights = Weights.objects.first()
        old_weights = testWeights.weights_int_list
        new_weights = '.'.join(["1"] * 208)
        testWeights.setWeightsWeights(new_weights)
        self.assertNotEqual(testWeights.weights_int_list, new_weights)
        self.assertEqual(testWeights.weights_int_list, old_weights)


    def test_setWeightsBiasSuccess(self):
        testWeights = Weights.objects.first()
        old_bias = testWeights.bias_int_list
        new_bias = [0] * 21
        self.assertTrue(testWeights.setWeightsBias(new_bias))
        self.assertEqual(testWeights.bias_int_list, ",".join("0" * 21))
        self.assertNotEqual(testWeights.bias_int_list, old_bias)

    def test_setWeightBiasFailureWrongBiasCount(self):
        testWeights = Weights.objects.first()
        old_bias = testWeights.bias_int_list
        new_bias = [0] * 20
        self.assertFalse(testWeights.setWeightsBias(new_bias))
        self.assertNotEqual(testWeights.bias_int_list, new_bias)
        self.assertEqual(testWeights.bias_int_list, old_bias)

    def test_setWeightBiasFailureWrongFormat(self):
        testWeights = Weights.objects.first()
        old_bias = testWeights.bias_int_list
        new_bias = '!'.join(["0"] * 21)
        self.assertFalse(testWeights.setWeightsBias(new_bias))
        self.assertNotEqual(testWeights.bias_int_list, new_bias)
        self.assertEqual(testWeights.bias_int_list, old_bias)


    def test_retrainWeights(self):
        testWeights = Weights.objects.first()
        old_weights = testWeights.weights_int_list
        testWeights.retrain()
        self.assertNotEqual(old_weights, testWeights.weights_int_list)

    def test_retrainBiases(self):
        testWeights = Weights.objects.first()
        old_biases = testWeights.bias_int_list
        testWeights.retrain()
        self.assertNotEqual(old_biases, testWeights.bias_int_list)



# Testing the methods for our neural network to predict moods
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
