import numpy as np
import matplotlib.image as pltim
import matplotlib.pyplot as plt
from PIL import Image


def read_image(filename):
    image_matrix = pltim.imread(filename)
    return image_matrix[:, :, 0]


def invert_colors(matrix):
    return 1 - matrix


def eliminate_whitespace(matrix):
    matrix = matrix[:, (matrix != 0).sum(axis=0) > 0]
    matrix = matrix[(matrix != 0).sum(axis=1) > 0, :]
    return matrix


def resize_image(matrix):
    img = Image.fromarray(matrix)
    img = img.resize((30, 30))
    return np.asarray(img)


def threshold_image(matrix, threshold):
    return 1.0 * (matrix > threshold)


def flatten_matrix(matrix):
    return matrix.reshape((1, matrix.size))


def display_processed_image(matrix):
    plt.imshow(matrix)
    plt.show()


def process_image(filename):
    image_matrix = read_image(filename)
    image_matrix = invert_colors(image_matrix)
    image_matrix = threshold_image(image_matrix, 0.1)
    image_matrix = eliminate_whitespace(image_matrix)
    image_matrix = resize_image(image_matrix)
    return flatten_matrix(image_matrix)


if __name__ == '__main__':
    image = process_image('l.png')
