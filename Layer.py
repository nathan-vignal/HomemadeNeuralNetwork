import numpy
import Neuron
class Layer():
    def __init__(self, nbNeurons):
        self.neurons = []
        for i  in range(nbNeurons):
            self.neurons.append(Neuron.Neuron(nbNeurons))


    def __str__(self):
        string = "Layer  "
        for neuron in self.neurons:
            string += str(neuron)
            string += " "
        return string

    def getMyActivations(self):
        array = []
        for neuron in self.neurons:
            array.append(neuron.getActivation())
        return array
    def getTheLastBatchActivations(self):
        array = []
        for neuron in self.neurons:
            array.append(neuron.getLastBatchActivation())
        return array


    def calculateMyNeuronsActivations(self, previousLayerActivation):
        for neuron in self.neurons:
            neuron.calculateActivation(previousLayerActivation)
