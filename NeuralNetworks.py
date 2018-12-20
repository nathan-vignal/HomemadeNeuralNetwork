import numpy
import Neuron
import Layer
import Output
import Network

network = Network.Network(4,5,numpy.array([[0,1,0,1,0],[0,1,0,1,0]]),numpy.array([[0.870880308832252, 0.870880308832252],
                                                                                  [0.8336463972003045, 0.8336463972003045],
                                                                                  [0.7733065427874742, 0.7733065427874742],
                                                                                  [0.938156133066739, 0.938156133066739],
                                                                                  [0.8610555876380515, 0.8610555876380515]] ))
network.feedForward()
print(network)

'''
entries = [1,0,0,0,1]
expectedOutput = [0,0,0,0,1]
biases = numpy.random.rand(5)
weights = numpy.random.rand(5,5)
weights = numpy.append(weights, numpy.random.rand(5,5))
print(weights)




hiddenLayer = numpy.multiply(entries, weights )
hiddenLayerActivation = []
for i in range(len(hiddenLayer)) :
    hiddenLayerActivation.append( numpy.sum(hiddenLayer[i]) + biases[i])

print(hiddenLayerActivation)
'''

