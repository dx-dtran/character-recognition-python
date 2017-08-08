import numpy as np

from logistic_function import logistic_function


def load_weights(filename):
    return np.loadtxt(filename)


def predict(weights1, weights2, image):
    im_size = image.shape[0]
    h1 = logistic_function(np.hstack((np.ones((im_size, 1)), image)).dot(weights1.T))
    h2 = logistic_function(np.hstack((np.ones((im_size, 1)), h1)).dot(weights2.T))
    conf = '{:0.2f}'.format(float(np.max(h2)) * 100)
    return list([chr(ord('a') + int(np.argmax(h2))), conf])


def make_prediction(image):
    weights1 = load_weights('weights1.txt')
    weights2 = load_weights('weights2.txt')
    return predict(weights1, weights2, image)


if __name__ == '__main__':
    main()
