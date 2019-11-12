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
    _network = []
    epochs = 20
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
        # network
        for i in range(4):
            self._network.append([])
        weightCounter = 0
        biasCounter = 0
        for i in range(11):
            self._network[0].append({'weights' : np.arange(weightCounter, weightCounter + 11, 1)})
            weightCounter += 11
            self._network[0][i]['bias'] = i
            biasCounter += 1
        for i in range(6):
            self._network[1].append({'weights' : np.arange(weightCounter, weightCounter + 11, 1)})
            weightCounter += 11
            self._network[1][i]['bias'] = i
            biasCounter += 1
        for i in range(3):
            self._network[2].append({'weights' : np.arange(weightCounter, weightCounter + 6, 1)})
            weightCounter += 6
            self._network[2][i]['bias'] = i
            biasCounter += 1
        self._network[3].append({'weights' : np.arange(weightCounter, weightCounter + 3, 1)})
        self._network[3][0]['bias'] = biasCounter

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
        layer1 = np.arange(11)
        weightCounter = 0
        biasCounter = 0
        # layer 1
        for i in range(layer1.shape[0]):
            h = 0
            for j in range(x.shape[0]):
                h += x[j] * self._weights["weight" + str(weightCounter)]
                weightCounter += 1
            sum = h + self._biases["bias" + str(biasCounter)]
            layer1[i] = self.activation(sum)
            biasCounter += 1

        # layer 2
        layer2 = np.arange(6)
        for i in range(layer2.shape[0]):
            h = 0
            for j in range(layer1.shape[0]):
                h += layer1[j] * self._weights["weight" + str(weightCounter)]
                weightCounter += 1
            sum = h + self._biases["bias" + str(biasCounter)]
            layer2[i] = self.activation(sum)
            biasCounter += 1

        # layer 3
        layer3 = np.arange(3)
        for i in range(layer3.shape[0]):
            h = 0
            for j in range(layer2.shape[0]):
                h += layer2[j] * self._weights["weight" + str(weightCounter)]
                weightCounter += 1
            sum = h + self._biases["bias" + str(biasCounter)]
            layer3[i] = self.activation(sum)
            biasCounter += 1

        output = 0
        for i in range(layer3.shape[0]):
            output += layer3[i] * self._weights["weight" + str(weightCounter)]
            weightCounter += 1
        sum = output + self._biases["bias" + str(biasCounter)]
        output = np.array([self.activation(sum)])
        if training:
            return layer1, layer2, layer3, output
        else:
            return output

    def activation(self, x):
        # activation function: sigmoid function
        return 1 / (1 + np.exp(-x))

    def deriv_activation(self, x):
        # Derivative of activation, normalized
        return x * (1 - x)

    def loss(self, y_true, y_pred):
        # y_true and y_pred are numpy arrays of the same length.
        # Mean squared error loss function
        return ((y_true - y_pred) ** 2).mean()

    # Backpropagate error and store in neurons
    def backward_propagate_error(self, y_true):
        for i in reversed(range(len(self._network))):
            layer = self._network[i]
            errors = list()
            if i != len(self._network)-1:
            	for j in range(len(layer)):
            		error = 0.0
            		for neuron in self._network[i + 1]:
            			error += (self._weights['weight' + str(neuron['weights'][j])] * neuron['delta'])
            		errors.append(error)
            else:
            	for j in range(len(layer)):
            		neuron = layer[j]
            		errors.append(-2*(y_true - neuron['output']))
            for j in range(len(layer)):
                neuron = layer[j]
                neuron['delta'] = errors[j] * self.deriv_activation(neuron['output'])

    # Update network weights with error
    def update_weights(self, data_input):
        print('-------------------------------updating weights-----------------------------')
        for i in range(len(self._network)):
            inputs = data_input[:]
            if i != 0:
                inputs = [neuron['output'] for neuron in self._network[i - 1]]
            for neuron in self._network[i]:
                print(neuron)
                for j in range(len(inputs)):
                    self._weights['weight' + str(neuron['weights'][j])] += self.learn_rate * neuron['delta'] * inputs[j]
                self._biases['bias' + str(neuron['bias'])] += self.learn_rate * neuron['delta']

    def train(self, data, all_y_trues):
        '''
        - data is a (n x 11) numpy array, n = # of samples in the dataset.
        - all_y_trues is a numpy array with n elements.
          Elements in all_y_trues correspond to those in data.
        '''
        for epoch in range(self.epochs):
            print('--------------------------ON epoch', epoch,'--------------------------')
            counter = 1
            for x, y_true in zip(data, all_y_trues):
                print('--------------------------data row', counter ,'--------------------------')
                counter += 1
                # --- Do a feedforward and save values
                layer1, layer2, layer3, output = self.feedforward(x, True)
                for i in range(layer1.shape[0]):
                    self._network[0][i]['output'] = layer1[i]
                for i in range(layer2.shape[0]):
                    self._network[1][i]['output'] = layer2[i]
                for i in range(layer3.shape[0]):
                    self._network[2][i]['output'] = layer3[i]
                self._network[3][0]['output'] = output[0]
                # print(output)
                print(self.loss(y_true, output[0]))

                # --- Calculate partial derivatives.
                self.backward_propagate_error(y_true)

                # --- Update weights and biases
                self.update_weights(x)

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
    # testModel = MoodNeuralNetwork()
    # testModel.setWeights("test_weights.json", True)
    # testModel.setBias("test_biases.json", True)
    # print(testModel.getBiases())
    # print(testModel.getWeights())
    # # #testModel.saveModel("test")
    # sampleData = np.arange(11)
    # print(testModel.feedforward(sampleData))
    print('------------------------------------------------------------')
    # Define dataset
    data = np.array([
      [-2, -1, -2, -1, -2, -1, -2, -1, -2, -1, 9],  # Alice
      [25, 6, 25, 6, 25, 6, 25, 6, 25, 6, 9],   # Bob
      [17, 4, 17, 4, 17, 4, 17, 4, 17, 4, 9],   # Charlie
      [-15, -6, -15, -6, -15, -6, -15, -6, -15, -6, 9], # Diana
    ])
    all_y_trues = np.array([
      1, # Alice
      0, # Bob
      0, # Charlie
      1, # Diana
    ])

    # Train our neural network!
    network = MoodNeuralNetwork()
    network.train(data, all_y_trues)
    pred = network.feedforward(data[0])
    print(pred)
    pred = network.feedforward(data[1])
    print(pred)
    pred = network.feedforward(data[2])
    print(pred)
    pred = network.feedforward(data[3])
    print(pred)
