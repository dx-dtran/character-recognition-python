import numpy as np


def letter_to_vector(character):
    if ord(character) < 97 or ord(character) > 122:
        raise Exception('Must be ascii lowercase letter')
    vector_matrix = np.eye(26)
    index = ord(character) - 97
    vector = vector_matrix[index]
    return np.array(vector)


def vector_to_letter(vector):
    index = int(np.argmax(vector))
    return chr(ord('a') + index)


if __name__ == '__main__':
    print(type(letter_to_vector('b')))
    print(vector_to_letter(letter_to_vector('a')))
