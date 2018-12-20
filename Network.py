import numpy
import Layer
class Network():
    def __init__(self,nbLayers,nbNeurons,entry,expectecOutput):
        cost = []
        self.entry = entry
        self.expectedOutput = expectecOutput
        self.layers = []
        for i in range(nbLayers):
            self.layers.append(Layer.Layer(nbNeurons))

    def __str__(self):
        string = "Network :\n"
        string += "Input "
        string += str(self.entry)
        string += "\n"
        i = 1
        for layer in self.layers:
            string += str(i)
            string += str(layer)
            string += "\n"
            i += 1
        return string

    def feedForward(self):
        for i in range(len(self.entry)):
            self.layers[0].calculateMyNeuronsActivations(self.entry[i])
            for i in range(1,len(self.layers)):
                previousLayerActivations = self.layers[i-1].getTheLastBatchActivations()
                self.layers[i].calculateMyNeuronsActivations(previousLayerActivations)


    def calculateCost(self):
        outputs = self.layers[len(self.layers)-1].getMyActivations()
        #[[0.870880308832252, 0.870880308832252], [0.8336463972003045, 0.8336463972003045], [0.7733065427874742, 0.7733065427874742], [0.938156133066739, 0.938156133066739], [0.8610555876380515, 0.8610555876380515]]
        i = 0
        for bacthNumber in range(len(self.entry)):
            for neuron in outputs:
                #activation = neuron[batchnumber]
                #
                self.expectedOutput = neuron









