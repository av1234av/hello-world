from numpy import dot, exp, random, array, where
import scipy.io as sio
from sklearn.model_selection import train_test_split
from matplotlib import pyplot

def basic_net():

    input_array=array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    output_array=array([[0,1,1,0]]).T

    random.seed(1)

    synaptic_weights = 2 * random.random((3,1)) - 1
    for iteration in xrange(10000):
        output = 1/(1 + exp(-(dot(input_array, synaptic_weights))))
        synaptic_weights += dot(input_array.T, (output_array - output) * output * (1 - output))

    print 1 / (1 + exp(-(dot([1,0,0], synaptic_weights))))

def using_scipy():
    mat_contents = sio.loadmat('C:\Users\\amit_\Downloads\machine-learning-ex4\machine-learning-ex4\ex4\ex4data1.mat')
    labels=mat_contents['y']
    lables=where(labels==10, 0, labels)
    labels=labels.reshape((labels.shape[0],))
    X_train, X_test, y_train, y_test = train_test_split(mat_contents['X'],labels)
    X_train, X_val = X_train[:-1000], X_train[-1000:]
    y_train, y_val = y_train[:-1000], y_train[-1000:]
    return X_train, y_train

def show_fig(X_train):
    for i in range(20):
        pyplot.imshow(X_train[100+i].reshape((20,20), order='F'), cmap='Greys', interpolation='nearest')

if __name__ == '__main__':
    X_train, y_train = using_scipy()
    # show_fig(X_train=X_train)