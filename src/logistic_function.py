import numpy as np


def logistic_function(x):
    return 1.0 / (1.0 + np.exp(-x))


def logistic_gradient(x):
    return logistic_function(x) * (1 - logistic_function(x))


if __name__ == '__main__':
    x = np.array([[1, 2, 3], [2, 3, 4]])
    print(logistic_function(x))