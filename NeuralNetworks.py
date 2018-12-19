import numpy



entries = [1,0,0,0,1]
expectedOutput = [0,0,0,0,1]
biases = numpy.random.rand(5)
weights = numpy.random.rand(5,5)
print(biases)



hiddenLayer = numpy.multiply(entries, weights )
print(numpy.sum(hiddenLayer[0]))
hiddenLayerActivation = []
for i in range(len(hiddenLayer)) :
    hiddenLayerActivation.append( numpy.sum(hiddenLayer[i]) + biases[i])

print(hiddenLayerActivation)


