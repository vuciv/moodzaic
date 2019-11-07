from django.test import TestCase
from mood_model.models import Weights
from users.models import User
from mood_model.sample_neural_network import MoodNeuralNetwork

# Create your tests here.

class WeightsTestCase(TestCase):
    def setUp(self):
        User.objects.create(username = "user1", password = "password1")
        User.objects.create(username = "user2", password = "password2")

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
        new_weights = ','.join(["1"] * 208)
        testWeights.setWeightsWeights(new_weights)
        self.assertEqual(testWeights.weights_int_list, new_weights)
        self.assertNotEqual(testWeights.weights_int_list, old_weights)

    def test_setWeightsWeightsFailureWrongWeightCount(self):
        testWeights = Weights.objects.first()
        old_weights = testWeights.weights_int_list
        new_weights = ','.join(["1"] * 207)
        testWeights.setWeightsWeights(new_weights)
        self.assertNotEqual(testWeights.weights_int_list, new_weights)
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
        new_bias = ','.join(["0"] * 21)
        testWeights.setWeightsBias(new_bias)
        self.assertEqual(testWeights.bias_int_list, new_bias)
        self.assertNotEqual(testWeights.bias_int_list, old_bias)

    def test_setWeightBiasFailureWrongBiasCount(self):
        testWeights = Weights.objects.first()
        old_bias = testWeights.bias_int_list
        new_bias = ','.join(["0"] * 20)
        testWeights.setWeightsBias(new_bias)
        self.assertNotEqual(testWeights.bias_int_list, new_bias)
        self.assertEqual(testWeights.bias_int_list, old_bias)

    def test_setWeightBiasFailureWrongFormat(self):
        testWeights = Weights.objects.first()
        old_bias = testWeights.bias_int_list
        new_bias = '!'.join(["0"] * 21)
        testWeights.setWeightsBias(new_bias)
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

    
        

