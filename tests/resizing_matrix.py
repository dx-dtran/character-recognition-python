import numpy as np


if __name__ == '__main__':
    x = np.array([[0, 0, 0, 1, 1, 1, 1],
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 1, 0, 0, 0]])

    print(x[:, (x != 0).sum(axis=0) > 0])
    print(x[(x != 0).sum(axis=1) > 0, :])
