import numpy
class Neuron():
    def __init__(self,nbNeuronsPreviousLayer):
        self.weights = numpy.random.rand(1,nbNeuronsPreviousLayer)
        self.bias = numpy.random.randint(-1,1)
        self.activation = []

    def calculateActivation(self, previousLayeractivations):
        self.activation.append(self.sigmoid(numpy.sum(numpy.multiply(previousLayeractivations, self.weights )) + self.bias))


    def sigmoid(self, activation):
        return 1/(1+(numpy.exp(-activation)))


    def __str__(self):
        string = str(self.activation)
        return string

    def getActivation(self):
        return self.activation

    def getLastBatchActivation(self):
        return self.activation[len(self.activation)-1]


