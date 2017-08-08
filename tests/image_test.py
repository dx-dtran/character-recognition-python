import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    a = np.tile(np.arange(255), (255, 1))
    plt.imshow(a)
    plt.show()
