import numpy as np
import random
import json

class MoodNeuralNetwork:
    '''
    A neural network with:
    - 11 inputs
    - a hidden layer with 11 neurons (h1... h11)
    - a hidden layer with 6 neurons (h1... h6)
    - a hidden layer with 3 neurons (h1... h3)
    - an output layer with 1 neuron (o1)
    '''
    _weights = {}
    _biases = {}
    epochs = 1000
    learn_rate = 0.1 # number of times to loop through the entire dataset

    def __init__(self, weights = None, biases = None):
        # Weights
        if weights:
            if len(weights) != 208:
                raise ValueError("There must be 208 weights for the model")
            self.setWeights(weights)
        else:
            for i in range(208):
                self._weights["weight" + str(i)] = np.random.normal()
        # biases
        if biases:
            if len(biases) != 21:
                raise ValueError("Number of biases must be 21")
            self.setBias(biases)
        else:
            for i in range(21):
                self._biases["bias" + str(i)] = np.random.uniform()

    def getWeights(self):
        return self._weights

    def getBiases(self):
        return self._biases

    def setWeights(self, newWeights, filename = False):
        if filename:
            with open(newWeights, 'r') as fp:
                weights = json.load(fp)
            if len(weights) != 208:
                raise ValueError("There must be 208 weights for the model")
            self._weights = weights
        else:
            self._weights = newWeights

    def setBias(self, newBiases, filename = False):
        if filename:
            with open(newBiases, 'r') as fp:
                biases = json.load(fp)
            if len(biases) != 21:
                raise ValueError("Number of biases must be 21")
            self._biases = biases
        else:
            self._biases = newBiases

    def feedforward(self, x, training = False):
        # x is a numpy array with 11 elements.
        layer1_sums = np.arange(11)
        layer1 = np.arange(11)
        weightCounter = 0
        biasCounter = 0
        # layer 1
        for i in range(layer1.shape[0]):
            h = 0
            for j in range(x.shape[0]):
                h += x[j] * self._weights["weight" + str(weightCounter)]
                weightCounter += 1
            layer1_sums[i] = h + self._biases["bias" + str(biasCounter)]
            layer1[i] = self.activation(layer1_sums[i])
            biasCounter += 1

        # layer 2
        layer2_sums = np.arange(6)
        layer2 = np.arange(6)
        for i in range(layer2.shape[0]):
            h = 0
            for j in range(layer1.shape[0]):
                h += layer1[j] * self._weights["weight" + str(weightCounter)]
                weightCounter += 1
            layer2_sums[i] = h + self._biases["bias" + str(biasCounter)]
            layer2[i] = self.activation(layer2_sums[i])
            biasCounter += 1

        # layer 3
        layer3_sums = np.arange(3)
        layer3 = np.arange(3)
        for i in range(layer3.shape[0]):
            h = 0
            for j in range(layer2.shape[0]):
                h += layer2[j] * self._weights["weight" + str(weightCounter)]
                weightCounter += 1
            layer3_sums[i] = h + self._biases["bias" + str(biasCounter)]
            layer3[i] = self.activation(layer3_sums[i])
            biasCounter += 1

        output = 0
        output_sum = 0
        for i in range(layer3_sums.shape[0]):
            output += layer3_sums[i] * self._weights["weight" + str(weightCounter)]
            weightCounter += 1
        output_sum = output + self._biases["bias" + str(biasCounter)]
        output = self.activation(output_sum)
        if training:
            return layer1_sums, layer1, layer2_sums, layer2, layer3_sums, layer3, output_sum, output
        else:
            return output

    def activation(self, x):
        # activation function: sigmoid function
        return 1 / (1 + np.exp(-x))

    def deriv_activation(self, x):
        # Derivative of activation, normalized
        fx = activation(x)
        return fx * (1 - fx)

    def loss(self, y_true, y_pred):
        # y_true and y_pred are numpy arrays of the same length.
        # Mean squared error loss function
        return ((y_true - y_pred) ** 2).mean()

    def train(self, data, all_y_trues):
        '''
        - data is a (n x 11) numpy array, n = # of samples in the dataset.
        - all_y_trues is a numpy array with n elements.
          Elements in all_y_trues correspond to those in data.
        '''
        learn_rate = 0.1
        epochs = 1000

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # --- Do a feedforward and save values
                layer1_sums, layer1, layer2_sums, layer2, layer3_sums, layer3, output_sum, output = self.feedforward(x)

                # --- Calculate partial derivatives.
                # --- Naming: d_L_d_w1 represents "partial L / partial w1"
                d_L_d_ypred = -2 * (y_true - y_pred)

                # ouput layer
                d_ypred_d_w205 = layer3[0] * deriv_sigmoid(output_sum)
                d_ypred_d_w206 = layer3[1] * deriv_sigmoid(output_sum)
                d_ypred_d_w207 = layer3[2] * deriv_sigmoid(output_sum)
                d_ypred_d_b21 = deriv_sigmoid(output_sum)

                d_ypred_d_l3_0 = self.w205 * deriv_sigmoid(output_sum)
                d_ypred_d_l3_1 = self.w206 * deriv_sigmoid(output_sum)
                d_ypred_d_l3_2 = self.w207 * deriv_sigmoid(output_sum)

                # layer 3
                d_ypred_d_w199 = layer2[0] * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_w200 = layer2[1] * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_w201 = layer2[2] * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_w202 = layer2[3] * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_w203 = layer2[4] * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_w204 = layer2[5] * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_b20 = deriv_sigmoid(layer3_sums[2])

                d_ypred_d_l2_0 = self.w199 * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_l2_1 = self.w200 * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_l2_2 = self.w201 * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_l2_3 = self.w202 * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_l2_4 = self.w203 * deriv_sigmoid(layer3_sums[2])
                d_ypred_d_l2_5 = self.w204 * deriv_sigmoid(layer3_sums[2])


                # layer 2
                # layer 1

                # --- Update weights and biases
                pass

                # --- Calculate total loss at the end of each epoch
                if epoch % 10 == 0:
                    y_preds = np.apply_along_axis(self.feedforward, 1, data)
                    loss = self.loss(all_y_trues, y_preds)
                    print("Epoch %d loss: %.3f" % (epoch, loss))

    def saveModel(self, filename):
        with open(filename + '_weights.json', 'w') as fp:
            json.dump(self._weights, fp)
        with open(filename + '_biases.json', 'w') as fp:
            json.dump(self._biases, fp)

if __name__ == "__main__":
    testModel = MoodNeuralNetwork()
    print(testModel.getBiases())
    print(testModel.getWeights())
    # testModel.setWeights("test_weights.json", True)
    # testModel.setBias("test_biases.json", True)
    #testModel.saveModel("test")
    sampleData = np.arange(11)
    print(testModel.feedforward(sampleData))
