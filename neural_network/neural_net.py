from numpy import dot, exp, random, array

input_array=array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
output_array=array([[0,1,1,0]]).T

random.seed(1)

synaptic_weights = 2 * random.random((3,1)) - 1
for iteration in xrange(10000):
    output = 1/(1 + exp(-(dot(input_array, synaptic_weights))))
    synaptic_weights += dot(input_array.T, (output_array - output) * output * (1 - output))

print 1 / (1 + exp(-(dot([1,0,0], synaptic_weights))))