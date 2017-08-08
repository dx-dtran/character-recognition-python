import numpy as np
import matplotlib.pyplot as plt


def get_image_vector(line):
    return np.fromstring(line, sep=' ')


def get_image_matrix(image_vector):
    image_width = int(np.round(np.sqrt(image_vector.shape))[-1])
    matrix = np.zeros((image_width, image_width))
    for row in range(image_width):
        for col in range(image_width):
            matrix[row][col] = image_vector[row * image_width + col]
    return matrix


def display_image_from_line(line):
    image_vector = get_image_vector(line)
    image_matrix = get_image_matrix(image_vector)
    plt.imshow(image_matrix)
    plt.show()


def display_image_from_vector(image_vector):
    image_matrix = get_image_matrix(image_vector)
    plt.imshow(image_matrix)


def display_all_images(path):
    with open(path, 'r') as file:
        for line in file.readlines():
            display_image_from_line(line)


def main():
    display_all_images('.\\data\\letter.txt')


if __name__ == '__main__':
    main()
