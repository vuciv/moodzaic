import numpy as np

class MoodNeuralNetwork:
  '''
  A neural network with:
    - 11 inputs
    - a hidden layer with 11 neurons (h1... h11)
    - a hidden layer with 6 neurons (h1... h6)
    - a hidden layer with 3 neurons (h1... h3)
    - an output layer with 1 neuron (o1)
  '''
  def __init__(self, weights = None):
    # Weights

    # Biases
    pass

  def feedforward(self, x):
    # x is a numpy array with 11 elements.
    return "Todo"

  def activation(self, x):
    # activation function
    return "Todo"

  def deriv_activation(self, x):
    # Derivative of activation
    return "Todo"

  def loss(self, y_true, y_pred):
    # y_true and y_pred are numpy arrays of the same length.
    return "Todo"

  def train(self, data, all_y_trues):
    '''
    - data is a (n x 11) numpy array, n = # of samples in the dataset.
    - all_y_trues is a numpy array with n elements.
      Elements in all_y_trues correspond to those in data.
    '''
    learn_rate = 0.1
    epochs = 1000 # number of times to loop through the entire dataset

    for epoch in range(epochs):
      for x, y_true in zip(data, all_y_trues):
        # --- Do a feedforward (we'll need these values later)
        pass

        # --- Calculate partial derivatives.
        # --- Naming: d_L_d_w1 represents "partial L / partial w1"
        pass

        # --- Update weights and biases
        pass

      # --- Calculate total loss at the end of each epoch
      #if epoch % 10 == 0:
        #y_preds = np.apply_along_axis(self.feedforward, 1, data)
        #loss = self.loss(all_y_trues, y_preds)
        #print("Epoch %d loss: %.3f" % (epoch, loss))
